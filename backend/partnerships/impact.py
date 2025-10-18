from fastapi import APIRouter

router = APIRouter()

@router.get("/report/")
def get_impact():
    return {"youth_engaged": 12000, "regions": 15}
