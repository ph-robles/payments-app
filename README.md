-- ============================================================
-- EXTENSÕES
-- ============================================================
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- ============================================================
-- TABELAS CORE
-- ============================================================

-- Perfis de usuário (espelha auth.users)
CREATE TABLE profiles (
  id            UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email         TEXT NOT NULL,
  full_name     TEXT,
  avatar_url    TEXT,
  plan          TEXT NOT NULL DEFAULT 'free' CHECK (plan IN ('free', 'pro', 'enterprise')),
  study_goal_minutes_daily INT DEFAULT 120,
  target_exam   TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Editais de concursos
CREATE TABLE editais (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  name        TEXT NOT NULL,
  banca       TEXT,
  cargo       TEXT,
  exam_date   DATE,
  is_active   BOOLEAN DEFAULT TRUE,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Matérias
CREATE TABLE materias (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  edital_id       UUID REFERENCES editais(id) ON DELETE SET NULL,
  name            TEXT NOT NULL,
  description     TEXT,
  color           TEXT DEFAULT '#6366f1',
  icon            TEXT DEFAULT 'BookOpen',
  weight          NUMERIC(3,2) DEFAULT 1.0,  -- peso no edital
  total_questions INT DEFAULT 0,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Tópicos dentro de matérias
CREATE TABLE topicos (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  materia_id  UUID NOT NULL REFERENCES materias(id) ON DELETE CASCADE,
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  name        TEXT NOT NULL,
  order_index INT DEFAULT 0,
  mastery     NUMERIC(5,2) DEFAULT 0 CHECK (mastery BETWEEN 0 AND 100),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- FLASHCARDS
-- ============================================================

CREATE TABLE flashcard_decks (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  materia_id  UUID REFERENCES materias(id) ON DELETE SET NULL,
  topico_id   UUID REFERENCES topicos(id) ON DELETE SET NULL,
  name        TEXT NOT NULL,
  description TEXT,
  is_ai_generated BOOLEAN DEFAULT FALSE,
  card_count  INT DEFAULT 0,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE flashcards (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  deck_id         UUID NOT NULL REFERENCES flashcard_decks(id) ON DELETE CASCADE,
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  front           TEXT NOT NULL,
  back            TEXT NOT NULL,
  hint            TEXT,
  tags            TEXT[],
  -- SM-2 fields
  ease_factor     NUMERIC(4,2) DEFAULT 2.5,
  interval        INT DEFAULT 1,           -- dias
  repetitions     INT DEFAULT 0,
  next_review_at  TIMESTAMPTZ DEFAULT NOW(),
  last_review_at  TIMESTAMPTZ,
  -- Stats
  total_reviews   INT DEFAULT 0,
  correct_reviews INT DEFAULT 0,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE flashcard_reviews (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  flashcard_id UUID NOT NULL REFERENCES flashcards(id) ON DELETE CASCADE,
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  quality     INT NOT NULL CHECK (quality BETWEEN 0 AND 5),  -- SM-2 quality
  time_taken_ms INT,
  reviewed_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- QUESTÕES
-- ============================================================

CREATE TABLE questoes (
  id            UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id       UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  materia_id    UUID REFERENCES materias(id) ON DELETE SET NULL,
  topico_id     UUID REFERENCES topicos(id) ON DELETE SET NULL,
  type          TEXT NOT NULL CHECK (type IN ('multiple_choice', 'true_false', 'essay')),
  difficulty    TEXT NOT NULL DEFAULT 'medium' CHECK (difficulty IN ('easy', 'medium', 'hard')),
  statement     TEXT NOT NULL,
  options       JSONB,     -- [{id, text, is_correct}]
  correct_answer TEXT,
  explanation   TEXT,
  source        TEXT,      -- 'ai_generated', 'pdf_extracted', 'manual'
  tags          TEXT[],
  embedding     vector(1536),  -- para busca semântica
  created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE questao_attempts (
  id            UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  questao_id    UUID NOT NULL REFERENCES questoes(id) ON DELETE CASCADE,
  user_id       UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  simulado_id   UUID,
  user_answer   TEXT,
  is_correct    BOOLEAN,
  time_taken_ms INT,
  attempted_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- SIMULADOS
-- ============================================================

CREATE TABLE simulados (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  name            TEXT NOT NULL,
  type            TEXT DEFAULT 'adaptive' CHECK (type IN ('adaptive', 'fixed', 'custom')),
  status          TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed')),
  total_questions INT NOT NULL,
  time_limit_min  INT,
  score           NUMERIC(5,2),
  started_at      TIMESTAMPTZ,
  finished_at     TIMESTAMPTZ,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE simulado_questions (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  simulado_id UUID NOT NULL REFERENCES simulados(id) ON DELETE CASCADE,
  questao_id  UUID NOT NULL REFERENCES questoes(id),
  order_index INT NOT NULL,
  user_answer TEXT,
  is_correct  BOOLEAN,
  time_taken_ms INT
);

-- ============================================================
-- PDFs E CONTEÚDO
-- ============================================================

CREATE TABLE pdf_uploads (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  materia_id      UUID REFERENCES materias(id) ON DELETE SET NULL,
  filename        TEXT NOT NULL,
  storage_path    TEXT NOT NULL,  -- Supabase Storage path
  file_size_bytes BIGINT,
  page_count      INT,
  status          TEXT DEFAULT 'processing' CHECK (status IN ('processing', 'ready', 'error')),
  extracted_text  TEXT,
  summary         TEXT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE pdf_chunks (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  pdf_id      UUID NOT NULL REFERENCES pdf_uploads(id) ON DELETE CASCADE,
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  content     TEXT NOT NULL,
  page_number INT,
  chunk_index INT,
  embedding   vector(1536),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- SESSÕES DE ESTUDO
-- ============================================================

CREATE TABLE study_sessions (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  materia_id      UUID REFERENCES materias(id) ON DELETE SET NULL,
  topico_id       UUID REFERENCES topicos(id) ON DELETE SET NULL,
  session_type    TEXT CHECK (session_type IN ('flashcard', 'questoes', 'leitura', 'tutor', 'simulado')),
  duration_min    INT,
  xp_earned       INT DEFAULT 0,
  started_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  ended_at        TIMESTAMPTZ
);

-- ============================================================
-- CRONOGRAMA
-- ============================================================

CREATE TABLE cronogramas (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  edital_id   UUID REFERENCES editais(id) ON DELETE CASCADE,
  name        TEXT NOT NULL,
  is_active   BOOLEAN DEFAULT TRUE,
  ai_version  INT DEFAULT 1,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE cronograma_items (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  cronograma_id   UUID NOT NULL REFERENCES cronogramas(id) ON DELETE CASCADE,
  materia_id      UUID NOT NULL REFERENCES materias(id) ON DELETE CASCADE,
  topico_id       UUID REFERENCES topicos(id) ON DELETE SET NULL,
  scheduled_date  DATE NOT NULL,
  duration_min    INT NOT NULL,
  is_completed    BOOLEAN DEFAULT FALSE,
  completed_at    TIMESTAMPTZ,
  order_index     INT DEFAULT 0
);

-- ============================================================
-- CHAT / TUTOR IA
-- ============================================================

CREATE TABLE chat_sessions (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  materia_id  UUID REFERENCES materias(id) ON DELETE SET NULL,
  title       TEXT,
  mode        TEXT DEFAULT 'tutor' CHECK (mode IN ('tutor', 'feynman', 'quiz', 'resumo')),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE chat_messages (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  session_id      UUID NOT NULL REFERENCES chat_sessions(id) ON DELETE CASCADE,
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  role            TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
  content         TEXT NOT NULL,
  tokens_used     INT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ============================================================
-- GAMIFICAÇÃO (base para features futuras)
-- ============================================================

CREATE TABLE user_achievements (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  achievement_key TEXT NOT NULL,
  earned_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(user_id, achievement_key)
);

CREATE TABLE daily_streaks (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  streak_date DATE NOT NULL,
  xp_earned   INT DEFAULT 0,
  UNIQUE(user_id, streak_date)
);

-- ============================================================
-- ÍNDICES DE PERFORMANCE
-- ============================================================

CREATE INDEX idx_flashcards_next_review ON flashcards(user_id, next_review_at);
CREATE INDEX idx_flashcards_deck ON flashcards(deck_id);
CREATE INDEX idx_questoes_materia ON questoes(materia_id, difficulty);
CREATE INDEX idx_questoes_embedding ON questoes USING ivfflat (embedding vector_cosine_ops);
CREATE INDEX idx_pdf_chunks_embedding ON pdf_chunks USING ivfflat (embedding vector_cosine_ops);
CREATE INDEX idx_study_sessions_user_date ON study_sessions(user_id, started_at);
CREATE INDEX idx_chat_messages_session ON chat_messages(session_id, created_at);
CREATE INDEX idx_cronograma_items_date ON cronograma_items(cronograma_id, scheduled_date);

-- ============================================================
-- ROW LEVEL SECURITY (RLS)
-- ============================================================

ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE editais ENABLE ROW LEVEL SECURITY;
ALTER TABLE materias ENABLE ROW LEVEL SECURITY;
ALTER TABLE topicos ENABLE ROW LEVEL SECURITY;
ALTER TABLE flashcard_decks ENABLE ROW LEVEL SECURITY;
ALTER TABLE flashcards ENABLE ROW LEVEL SECURITY;
ALTER TABLE flashcard_reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE questoes ENABLE ROW LEVEL SECURITY;
ALTER TABLE questao_attempts ENABLE ROW LEVEL SECURITY;
ALTER TABLE simulados ENABLE ROW LEVEL SECURITY;
ALTER TABLE pdf_uploads ENABLE ROW LEVEL SECURITY;
ALTER TABLE pdf_chunks ENABLE ROW LEVEL SECURITY;
ALTER TABLE study_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE cronogramas ENABLE ROW LEVEL SECURITY;
ALTER TABLE cronograma_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE chat_messages ENABLE ROW LEVEL SECURITY;

-- Políticas RLS (padrão: usuário acessa apenas seus dados)
DO $$
DECLARE
  tbl TEXT;
  tables TEXT[] := ARRAY[
    'profiles','editais','materias','topicos',
    'flashcard_decks','flashcards','flashcard_reviews',
    'questoes','questao_attempts','simulados',
    'pdf_uploads','pdf_chunks','study_sessions',
    'cronogramas','cronograma_items','chat_sessions','chat_messages'
  ];
BEGIN
  FOREACH tbl IN ARRAY tables LOOP
    EXECUTE format(
      'CREATE POLICY "Users access own data" ON %I FOR ALL USING (auth.uid() = user_id)',
      tbl
    );
  END LOOP;
END $$;

-- ============================================================
-- TRIGGERS
-- ============================================================

-- Auto-criar perfil ao registrar
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO profiles (id, email, full_name)
  VALUES (NEW.id, NEW.email, NEW.raw_user_meta_data->>'full_name');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION handle_new_user();

-- Updated_at automático
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = NOW(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_updated_at BEFORE UPDATE ON profiles
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
