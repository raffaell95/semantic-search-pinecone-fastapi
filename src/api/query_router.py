from fastapi import APIRouter
from src.services.query_service import query_samples

router = APIRouter()

@router.post("/api/query", summary="Query the database")
async def query(search: str):
    response = query_samples(search=search)

    matches = response.matches
    json_response = [{"id": match.id, "score": match.score, "metadata": match.metadata} for match in matches]

    return json_response