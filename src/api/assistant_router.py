from fastapi import APIRouter
from src.services.query_service import query_samples
from src.services.assistant_service import assistant_question

router = APIRouter()

@router.post("/api/assistant/query", summary="Query the database vector simple and return a inteligent response")
async def assistant_query(search: str):

    response_dbcector_extract = query_samples(search=search)

    response = assistant_question(question=search, short_extract=response_dbcector_extract)

    return response