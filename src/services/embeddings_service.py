from openai.types import CreateEmbeddingResponse
from src.services.authentication_service import authenticate_openai


client_openai = authenticate_openai()

def embeddings_service(chuck: str) -> CreateEmbeddingResponse:
    embedding =  client_openai.embeddings.create(
        model="text-embedding-3-small",
        input=chuck
    )

    response = embedding.to_dict()
    vector = response["data"][0]["embedding"]

    return vector
