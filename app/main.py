from fastapi import FastAPI

from app.services.health_service import HealthService
from app.api.projects import router as projects_router


app = FastAPI(
    title="IssueFlow API",
    description="Team Issue and Incident Management API",
    version="1.0.0"
)

health_service = HealthService()


app.include_router(projects_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IssueFlow API"
    }


@app.get("/health")
def health_check():
    return health_service.get_status()