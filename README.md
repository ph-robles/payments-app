from openai import AsyncOpenAI
from typing import AsyncGenerator
from app.config import get_settings

settings = get_settings()
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

TUTOR_SYSTEM_PROMPT = """Você é um tutor especializado em concursos públicos brasileiros.

Seu estilo:
- Linguagem clara, didática e encorajadora
- Use analogias do cotidiano para explicar conceitos complexos
- Aplique o Método Feynman: explique como se fosse para uma criança de 12 anos
- Estruture respostas com: conceito central → contexto → exemplos → dica de prova
- Destaque pontos que mais caem em provas com 🎯
- Use ✅ para conceitos corretos e ❌ para erros comuns
- Sempre termine com: "Quer que eu aprofunde algum ponto?"

Matéria do estudante: {materia}
Nível estimado: {nivel}
"""

async def stream_tutor_response(
    messages: list[dict],
    materia: str = "Geral",
    nivel: str = "intermediário"
) -> AsyncGenerator[str, None]:
    """Gera resposta do tutor com streaming."""
    system_prompt = TUTOR_SYSTEM_PROMPT.format(materia=materia, nivel=nivel)
    
    stream = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            *messages
        ],
        stream=True,
        temperature=0.7,
        max_tokens=2000,
    )
    
    async for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            yield delta.content

async def generate_flashcards(
    content: str,
    quantity: int = 10,
    materia: str = ""
) -> list[dict]:
    """Gera flashcards a partir de um conteúdo."""
    prompt = f"""
    Crie exatamente {quantity} flashcards de estudo sobre: {materia}
    
    Conteúdo base:
    {content[:4000]}
    
    Retorne APENAS um JSON válido no formato:
    {{
      "flashcards": [
        {{
          "front": "pergunta objetiva e clara",
          "back": "resposta completa com contexto",
          "hint": "dica opcional",
          "tags": ["tag1", "tag2"]
        }}
      ]
    }}
    
    Regras:
    - Foque no que mais cai em concursos
    - Perguntas diretas e objetivas
    - Respostas completas mas concisas
    - Varie os tipos: definição, aplicação, comparação
    """
    
    response = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.5,
    )
    
    import json
    data = json.loads(response.choices[0].message.content)
    return data.get("flashcards", [])

async def generate_questoes(
    content: str,
    quantity: int = 5,
    difficulty: str = "medium",
    question_type: str = "multiple_choice",
    materia: str = ""
) -> list[dict]:
    """Gera questões de concurso no estilo CESPE/FCC/FGV."""
    type_instructions = {
        "multiple_choice": "5 alternativas (A-E), apenas uma correta, estilo CESPE/FCC",
        "true_false": "afirmação para julgar Certo ou Errado, estilo CESPE",
        "essay": "questão dissertativa com pontos de resposta esperados"
    }
    
    prompt = f"""
    Crie {quantity} questões de concurso público sobre: {materia}
    Tipo: {type_instructions.get(question_type)}
    Dificuldade: {difficulty}
    
    Conteúdo base:
    {content[:4000]}
    
    Retorne APENAS JSON no formato:
    {{
      "questoes": [
        {{
          "statement": "enunciado da questão",
          "type": "{question_type}",
          "difficulty": "{difficulty}",
          "options": [
            {{"id": "A", "text": "alternativa", "is_correct": false}},
            {{"id": "B", "text": "alternativa", "is_correct": true}}
          ],
          "correct_answer": "B",
          "explanation": "explicação detalhada do gabarito com base legal se aplicável",
          "tags": ["tag1"]
        }}
      ]
    }}
    """
    
    response = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.6,
    )
    
    import json
    data = json.loads(response.choices[0].message.content)
    return data.get("questoes", [])

async def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """Gera embeddings para busca semântica."""
    response = await client.embeddings.create(
        model=settings.OPENAI_EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]

async def generate_study_plan(
    materias: list[dict],
    exam_date: str,
    daily_hours: float,
    performance_data: dict
) -> dict:
    """Gera cronograma de estudos personalizado com IA."""
    prompt = f"""
    Você é um especialista em planejamento de estudos para concursos públicos.
    
    Dados do estudante:
    - Matérias: {materias}
    - Data da prova: {exam_date}
    - Horas disponíveis por dia: {daily_hours}h
    - Desempenho atual: {performance_data}
    
    Crie um plano de estudos semanal otimizado considerando:
    1. Priorizar matérias com maior peso no edital
    2. Mais tempo nas matérias com menor desempenho
    3. Revisar matérias fortes periodicamente
    4. Deixar a última semana para revisão geral e simulados
    
    Retorne JSON com estrutura de cronograma semanal.
    """
    
    response = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.4,
    )
    
    import json
    return json.loads(response.choices[0].message.content)
