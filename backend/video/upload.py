from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()

@router.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    os.makedirs("videos", exist_ok=True)
    with open(f"videos/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
