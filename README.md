from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class SM2Result:
    ease_factor: float
    interval: int
    repetitions: int
    next_review_at: datetime

def calculate_sm2(
    quality: int,        # 0-5: qualidade da resposta
    ease_factor: float,  # fator de facilidade atual
    interval: int,       # intervalo atual em dias
    repetitions: int     # número de repetições
) -> SM2Result:
    """
    Implementação do algoritmo SM-2 para repetição espaçada.
    
    Quality:
    5 - resposta perfeita
    4 - resposta correta com leve hesitação
    3 - correto com dificuldade considerável
    2 - incorreto, mas ao ver a resposta pareceu fácil
    1 - incorreto, a resposta correta pareceu familiar
    0 - blackout total
    """
    if quality < 3:
        # Resetar intervalo se errou
        new_repetitions = 0
        new_interval = 1
    else:
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval * ease_factor)
        new_repetitions = repetitions + 1
    
    # Atualizar ease factor
    new_ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    new_ease_factor = max(1.3, new_ease_factor)  # mínimo 1.3
    
    next_review = datetime.utcnow() + timedelta(days=new_interval)
    
    return SM2Result(
        ease_factor=round(new_ease_factor, 2),
        interval=new_interval,
        repetitions=new_repetitions,
        next_review_at=next_review
    )
