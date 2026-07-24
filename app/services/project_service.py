from sqlalchemy.orm import Session

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:

    def __init__(self):
        self.repository = ProjectRepository()

    def create_project(
        self,
        db: Session,
        project: ProjectCreate
    ):
        return self.repository.create(
            db=db,
            project_data=project
        )

    def get_all_projects(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    def get_project_by_id(
        self,
        db: Session,
        project_id: int
    ):
        return self.repository.get_by_id(
            db=db,
            project_id=project_id
        )