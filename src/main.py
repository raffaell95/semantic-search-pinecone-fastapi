from fastapi import FastAPI
from src.api.index_router import router as api_index_router
from src.api.embeddings_router import router as api_embeddings_router
from src.api.miscellabeous_router import router as api_miscellabeous_router
from src.api.upsert_router import router as api_upsert_router
from src.api.query_router import router as api_query_router
from src.api.assistant_router import router as api_assistant_router

app = FastAPI()
app.include_router(api_index_router)
app.include_router(api_embeddings_router)
app.include_router(api_miscellabeous_router)
app.include_router(api_upsert_router)
app.include_router(api_query_router)
app.include_router(api_assistant_router)