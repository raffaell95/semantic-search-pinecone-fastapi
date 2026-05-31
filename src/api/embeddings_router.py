from _testcapi import awaitType

from src.services.embeddings_service import embeddings_service
from fastapi import APIRouter

router = APIRouter()

@router.post("/api/embeddings", summary="Create Embeddings by OpenAI")
async def embeddings_router(chuck: str):
    return embeddings_service(chuck)