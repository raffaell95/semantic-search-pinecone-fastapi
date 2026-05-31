import os
from src.services.authentication_service import authenticate_pinecone
from src.services.embeddings_service import embeddings_service
from dotenv import load_dotenv

pc = authenticate_pinecone()

load_dotenv()

def query_samples(search: str):

    pc = authenticate_pinecone()

    try:
        vectors = embeddings_service(search)

        index = pc.Index(host=os.getenv("PINECONE_HOST"))

        response = index.query(namespace="master-ia-pos", vector=vectors, top_k=10, include_metadata=True)

        return response
    except Exception as e:
        return {"error": str(e)}