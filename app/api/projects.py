from fastapi import APIRouter

from app.schemas.project import ProjectCreate
from app.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

project_service = ProjectService()


@router.post("/")
def create_project(project: ProjectCreate):
    return project_service.create_project(project)