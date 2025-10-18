from fastapi import FastAPI
app = FastAPI()

@app.get("/impact/")
def get_impact():
    return {"youth_engaged": 12000, "regions": 15}
