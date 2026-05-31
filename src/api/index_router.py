from fastapi import APIRouter

from src.services.index_service import create_index, list_index, detail_index

router = APIRouter()

@router.post("/api/index/create", summary="Create Index by Pinecone")
async def create_index_router(name_index: str):
     response = create_index(name_index)
     return {f'The index {response}'}

@router.get("/api/index/list", summary="List Index by Pinecone")
async def list_index_router():
     return list_index()

@router.post("/api/index/detail", summary="Show Details From Index")
async def detail_index_router(name_index: str):
     return detail_index(name_index)