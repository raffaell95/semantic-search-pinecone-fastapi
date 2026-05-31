from fastapi import APIRouter, UploadFile, File
from src.services.miscellabeous_service import extract_text_from_pdf, slip_text_into_chunks
from src.services.embeddings_service import embeddings_service

router = APIRouter()

@router.post("/api/miscellaneous/pdf", summary="Extract Text From a PDF")
async def pdf_to_text(pdf_file: UploadFile = File(...)):
    return extract_text_from_pdf(pdf_file)

@router.post("/api/miscellabeous/split-in-chunks", summary="Split Text Into Chunks")
async def split_in_chunks_samples(text: str):
    return slip_text_into_chunks(text)

@router.post("/api/miscellabeous/slip-in-chunks-embbedings", summary="")
async def split_in_chunks_embbedings(text: str):
    chunks_list = slip_text_into_chunks(text)

    try:
        embbedings = [ embeddings_service(chuck=chunk) for chunk in chunks_list]
        return embbedings
    except Exception as e:
        return {"error": str(e)}
