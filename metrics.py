from fastapi import FastAPI
app = FastAPI()

@app.get("/metrics/")
def get_metrics():
    return {"views": 120, "likes": 45, "shares": 30}
