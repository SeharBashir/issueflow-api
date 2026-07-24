from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.project import ProjectCreate
from app.services.project_service import ProjectService
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


project_service = ProjectService()


@router.post("/", status_code=201)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    return project_service.create_project(
        db=db,
        project=project
    )


@router.get("/")
def get_projects(
    db: Session = Depends(get_db)
):
    return project_service.get_all_projects(db)

@router.get("/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = project_service.get_project_by_id(
        db=db,
        project_id=project_id
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project