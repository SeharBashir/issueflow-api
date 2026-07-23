from app.schemas.project import ProjectCreate


class ProjectService:

    def create_project(self, project: ProjectCreate) -> dict:
        return {
            "id": 1,
            "name": project.name,
            "description": project.description
        }