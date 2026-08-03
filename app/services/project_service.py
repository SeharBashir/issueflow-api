from sqlalchemy.orm import Session

from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.core.exceptions import NotFoundException


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
        project = self.repository.get_by_id(
            db=db,
            project_id=project_id
        )

        if project is None:
            raise NotFoundException("Project", project_id)

        return project

    def update_project(
        self,
        db: Session,
        project_id: int,
        project_data: ProjectUpdate
    ):
        project = self.get_project_by_id(
            db=db,
            project_id=project_id
        )

        return self.repository.update(
            db=db,
            project=project,
            project_data=project_data
        )

    def delete_project(
        self,
        db: Session,
        project_id: int
    ):
        project = self.get_project_by_id(
            db=db,
            project_id=project_id
        )

        self.repository.delete(
            db=db,
            project=project
        )