from fastapi import FastAPI
from backend.video.upload import upload_video
from backend.analytics.metrics import get_metrics
from backend.partnerships.impact import get_impact

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to SIQNet API"}

# Register endpoints
app.include_router(upload_video)
app.include_router(get_metrics)
app.include_router(get_impact)
