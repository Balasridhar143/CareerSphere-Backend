from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.mongodb import mongodb

from app.api.routes.auth_routes import router as auth_router
from app.api.routes.recruiter_routes import router as recruiter_router
from app.api.routes.company_routes import router as company_router
from app.api.routes.job_routes import router as job_router
from app.api.routes.internship_routes import router as internship_router
from app.api.routes.hackathon_routes import router as hackathon_router
from app.api.routes.resume_routes import router as resume_router
from app.api.routes.ai_routes import router as ai_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb.connect()
    yield
    await mongodb.disconnect()


app = FastAPI(
    title="CareerSphere AI Backend",
    description="Agentic AI Career Platform Backend",
    version="1.0.0",
    lifespan=lifespan,
)

# -------------------------------
# CORS Configuration
# -------------------------------
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Routers
# -------------------------------

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    recruiter_router,
    prefix="/recruiter",
    tags=["Recruiter"]
)

app.include_router(
    company_router,
    prefix="/company",
    tags=["Company"]
)

app.include_router(
    job_router,
    prefix="/job",
    tags=["Jobs"]
)

app.include_router(
    internship_router,
    prefix="/internship",
    tags=["Internships"]
)

app.include_router(
    hackathon_router,
    prefix="/hackathon",
    tags=["Hackathons"]
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    ai_router,
    prefix="/ai",
    tags=["AI"]
)


@app.get("/")
async def home():
    return {
        "status": "success",
        "message": "CareerSphere AI Backend Running 🚀"
    }