from typing import Any

from src.services.authentication_service import authenticate_pinecone
from pinecone import ServerlessSpec, IndexModel, IndexList

pc = authenticate_pinecone()

def create_index(name: str) -> IndexModel:
    return pc.create_index(
        name=name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

def list_index() -> dict[str, Any]:
    return pc.list_indexes().to_dict()

def detail_index(name: str) -> dict[str, Any]:
    return pc.describe_index(name).to_dict()