from fastapi import FastAPI

app = FastAPI(
    title="CareerSphere AI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "CareerSphere AI Backend Running Successfully"
    }