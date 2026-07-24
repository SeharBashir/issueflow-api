from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


class ProjectRepository:

    def create(
        self,
        db: Session,
        project_data: ProjectCreate
    ) -> Project:

        project = Project(
            name=project_data.name,
            description=project_data.description
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    def get_all(
        self,
        db: Session
    ) -> list[Project]:

        return db.query(Project).all()

    def get_by_id(
        self,
        db: Session,
        project_id: int
    ) -> Project | None:

        return db.query(Project).filter(
            Project.id == project_id
        ).first()