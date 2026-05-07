-- Tabela de cidades personalizadas
CREATE TABLE cidades (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  nome TEXT NOT NULL,
  slug TEXT NOT NULL UNIQUE,
  estado TEXT NOT NULL,
  regiao TEXT,
  populacao INTEGER,
  destaque BOOLEAN DEFAULT false,
  ativo BOOLEAN DEFAULT true,
  criado_em TIMESTAMP DEFAULT NOW()
);

-- Tabela de provedores por cidade (já existe, mas vamos melhorar)
ALTER TABLE provedor_cidades ADD COLUMN IF NOT EXISTS personalizado BOOLEAN DEFAULT false;

-- Senha do painel admin
CREATE TABLE admin_config (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  chave TEXT NOT NULL UNIQUE,
  valor TEXT NOT NULL
);

INSERT INTO admin_config (chave, valor) VALUES
('admin_password', 'fibrado2026');
