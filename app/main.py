from fastapi import FastAPI

from app.api.routes.auth_routes import router as auth_router

app = FastAPI(
    title="CareerSphere AI Backend",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
async def home():

    return {
        "message": "CareerSphere AI Backend Running"
    }