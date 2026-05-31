import os
import uuid
from typing import List
from dotenv import load_dotenv

from pinecone import UpsertResponse

from src.services.embeddings_service import embeddings_service
from src.services.authentication_service import authenticate_pinecone

load_dotenv()

pc = authenticate_pinecone()

def upsert_service(embenddings: List[str]) -> UpsertResponse:
    index = pc.Index(host=os.getenv("PINECONE_HOST"))

    try:
        vectors = [{"id": f"{uuid.uuid4()}", "values": chuck_unit}
                   for chuck_unit in embenddings]

        index.upsert(vectors, namespace="master-ia-pos")
        return {"message": "Document upserted successfully"}
    except Exception as e:
        return {"error": str(e)}

def upsert_service_metadata(metadata: dict, chuck_list_text: list) -> UpsertResponse:
    index = pc.Index(host=os.getenv("PINECONE_HOST"))

    vectors = []

    try:
        for chuck_text in chuck_list_text:
            embedding_chuck = embeddings_service(chuck_text)
            metadata_complete = {**metadata, "chuck": chuck_text}
            vectors.append({"id": f"{uuid.uuid4()}", "values": embedding_chuck, "metadata": metadata_complete})

        response = index.upsert(vectors=vectors, namespace="master-ia-pos")

        return response["upserted_count"]
    except Exception as e:
        return {"error": str(e)}