from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.dependencies import get_current_user
from app.services.openai_service import stream_tutor_response
from app.schemas.tutor import ChatRequest, ChatSession
from app.db.supabase_client import get_supabase_client
import json

router = APIRouter(prefix="/tutor", tags=["Tutor IA"])

@router.post("/chat/stream")
async def chat_stream(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user)
):
    """Stream de resposta do tutor IA via SSE."""
    
    async def generate():
        try:
            async for token in stream_tutor_response(
                messages=request.messages,
                materia=request.materia or "Geral",
                nivel=request.nivel or "intermediário"
            ):
                # SSE format
                yield f"data: {json.dumps({'token': token})}\n\n"
            
            yield f"data: {json.dumps({'done': True})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        }
    )

@router.post("/sessions")
async def create_session(
    materia_id: str | None = None,
    mode: str = "tutor",
    current_user: dict = Depends(get_current_user)
):
    """Cria nova sessão de chat com o tutor."""
    supabase = get_supabase_client()
    
    result = supabase.table("chat_sessions").insert({
        "user_id": current_user["id"],
        "materia_id": materia_id,
        "mode": mode,
        "title": "Nova conversa"
    }).execute()
    
    return result.data[0]

@router.get("/sessions")
async def list_sessions(
    current_user: dict = Depends(get_current_user)
):
    """Lista sessões de chat do usuário."""
    supabase = get_supabase_client()
    
    result = supabase.table("chat_sessions")\
        .select("*, materias(name, color)")\
        .eq("user_id", current_user["id"])\
        .order("created_at", desc=True)\
        .limit(50)\
        .execute()
    
    return result.data

@router.post("/sessions/{session_id}/messages")
async def save_message(
    session_id: str,
    role: str,
    content: str,
    tokens_used: int = 0,
    current_user: dict = Depends(get_current_user)
):
    """Persiste mensagem na sessão."""
    supabase = get_supabase_client()
    
    result = supabase.table("chat_messages").insert({
        "session_id": session_id,
        "user_id": current_user["id"],
        "role": role,
        "content": content,
        "tokens_used": tokens_used
    }).execute()
    
    return result.data[0]
