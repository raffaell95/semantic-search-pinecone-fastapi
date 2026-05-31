import json
from fastapi import APIRouter, UploadFile, File, Form

from src.api.miscellabeous_router import split_in_chunks_samples
from src.api.miscellabeous_router import split_in_chunks_embbedings
from src.services.miscellabeous_service import extract_text_from_pdf
from src.services.upsert_service import upsert_service, upsert_service_metadata

router = APIRouter()

@router.post("/api/upsert/pdf", summary="Upsert a document PDF into the database")
async def upsert(file: UploadFile = File(...)):

    text_from_pdf = extract_text_from_pdf(file)
    chuncks_list_embbedings = await split_in_chunks_embbedings(text=text_from_pdf)
    return upsert_service(embenddings=chuncks_list_embbedings)

@router.post("/api/upsert/pdf_metadata", summary="Upsert a document PDF into the database with metadata")
async def upsert_metadata(file_pdf: UploadFile = File(...), metadata: str = Form(...)):

    try:
        metadata_json = json.loads(metadata)
        text_from_pdf = extract_text_from_pdf(file_pdf)
        chucks_list_text = await split_in_chunks_samples(text=text_from_pdf)
        response = upsert_service_metadata(metadata=metadata_json, chuck_list_text=chucks_list_text)

        return {"message": f"Successfully upserted {response} documents"}
    except Exception as e:
        return {"error": str(e)}

