from fastapi import FastAPI

from app.api.projects import router as projects_router
from app.database.connection import Base, engine
from app.models import Project
from app.services.health_service import HealthService
from app.api.issues import router as issues_router



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="IssueFlow API",
    description="Team Issue and Incident Management API",
    version="1.0.0"
)


health_service = HealthService()

app.include_router(projects_router)
app.include_router(issues_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to IssueFlow API"
    }


@app.get("/health")
def health_check():
    return health_service.get_status()