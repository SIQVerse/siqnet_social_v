from fastapi import APIRouter

router = APIRouter()

@router.get("/stats/")
def get_metrics():
    return {"views": 120, "likes": 45, "shares": 30}
