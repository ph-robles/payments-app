from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.dependencies import get_current_user
from app.services.openai_service import generate_flashcards
from app.services.sm2_service import calculate_sm2
from app.db.supabase_client import get_supabase_client
from app.schemas.flashcard import (
    FlashcardReviewRequest,
    GenerateFlashcardsRequest
)
from datetime import datetime, timezone

router = APIRouter(prefix="/flashcards", tags=["Flashcards"])

@router.get("/due")
async def get_due_flashcards(
    limit: int = 20,
    current_user: dict = Depends(get_current_user)
):
    """Retorna flashcards para revisar hoje (SM-2)."""
    supabase = get_supabase_client()
    now = datetime.now(timezone.utc).isoformat()
    
    result = supabase.table("flashcards")\
        .select("*, flashcard_decks(name, materia_id, materias(name, color))")\
        .eq("user_id", current_user["id"])\
        .lte("next_review_at", now)\
        .order("next_review_at")\
        .limit(limit)\
        .execute()
    
    return {
        "cards": result.data,
        "total_due": len(result.data)
    }

@router.post("/{flashcard_id}/review")
async def review_flashcard(
    flashcard_id: str,
    request: FlashcardReviewRequest,
    current_user: dict = Depends(get_current_user)
):
    """Processa revisão de flashcard aplicando SM-2."""
    supabase = get_supabase_client()
    
    # Buscar card atual
    card = supabase.table("flashcards")\
        .select("*")\
        .eq("id", flashcard_id)\
        .eq("user_id", current_user["id"])\
        .single()\
        .execute()
    
    if not card.data:
        raise HTTPException(status_code=404, detail="Flashcard não encontrado")
    
    c = card.data
    
    # Calcular novo intervalo SM-2
    result = calculate_sm2(
        quality=request.quality,
        ease_factor=float(c["ease_factor"]),
        interval=c["interval"],
        repetitions=c["repetitions"]
    )
    
    # Atualizar flashcard
    is_correct = request.quality >= 3
    supabase.table("flashcards").update({
        "ease_factor": result.ease_factor,
        "interval": result.interval,
        "repetitions": result.repetitions,
        "next_review_at": result.next_review_at.isoformat(),
        "last_review_at": datetime.now(timezone.utc).isoformat(),
        "total_reviews": c["total_reviews"] + 1,
        "correct_reviews": c["correct_reviews"] + (1 if is_correct else 0)
    }).eq("id", flashcard_id).execute()
    
    # Registrar review para analytics
    supabase.table("flashcard_reviews").insert({
        "flashcard_id": flashcard_id,
        "user_id": current_user["id"],
        "quality": request.quality,
        "time_taken_ms": request.time_taken_ms
    }).execute()
    
    return {
        "next_review_in_days": result.interval,
        "next_review_at": result.next_review_at.isoformat(),
        "is_correct": is_correct,
        "ease_factor": result.ease_factor
    }

@router.post("/generate")
async def generate_ai_flashcards(
    request: GenerateFlashcardsRequest,
    background_tasks: BackgroundTasks,
    current_user: dict = Depends(get_current_user)
):
    """Gera flashcards com IA a partir de um conteúdo."""
    supabase = get_supabase_client()
    
    # Criar deck
    deck = supabase.table("flashcard_decks").insert({
        "user_id": current_user["id"],
        "materia_id": request.materia_id,
        "name": request.deck_name or f"Deck IA - {request.materia_name}",
        "is_ai_generated": True
    }).execute()
    
    deck_id = deck.data[0]["id"]
    
    # Gerar flashcards com IA
    cards = await generate_flashcards(
        content=request.content,
        quantity=request.quantity,
        materia=request.materia_name or ""
    )
    
    # Inserir no banco
    cards_to_insert = [
        {
            "deck_id": deck_id,
            "user_id": current_user["id"],
            "front": card["front"],
            "back": card["back"],
            "hint": card.get("hint"),
            "tags": card.get("tags", [])
        }
        for card in cards
    ]
    
    supabase.table("flashcards").insert(cards_to_insert).execute()
    
    # Atualizar contagem do deck
    supabase.table("flashcard_decks").update({
        "card_count": len(cards)
    }).eq("id", deck_id).execute()
    
    return {
        "deck_id": deck_id,
        "cards_generated": len(cards),
        "message": f"{len(cards)} flashcards criados com sucesso!"
    }
