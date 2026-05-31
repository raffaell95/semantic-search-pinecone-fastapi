import os
from pinecone.grpc import PineconeGRPC as Pinecone, PineconeGRPC
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def authenticate_pinecone() -> Pinecone:
    return Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def authenticate_openai() -> OpenAI:
    return OpenAI(api_key=os.getenv("API_KEY_OPENAI"))