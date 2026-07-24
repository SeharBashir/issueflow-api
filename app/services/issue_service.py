
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.issue_repository import IssueRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.issue import IssueCreate


class IssueService:

    def __init__(self):
        self.issue_repository = IssueRepository()
        self.project_repository = ProjectRepository()

    def create_issue(
        self,
        db: Session,
        issue: IssueCreate
    ):
        # Check whether the project exists
        project = self.project_repository.get_by_id(
            db=db,
            project_id=issue.project_id
        )

        if project is None:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

        return self.issue_repository.create(
            db=db,
            issue_data=issue
        )

    def get_all_issues(
        self,
        db: Session
    ):
        return self.issue_repository.get_all(db)

    def get_issues_by_project(
        self,
        db: Session,
        project_id: int
    ):
        # Check whether the project exists
        project = self.project_repository.get_by_id(
            db=db,
            project_id=project_id
        )

        if project is None:
            raise HTTPException(
                status_code=404,
                detail="Project not found"
            )

        return self.issue_repository.get_by_project_id(
            db=db,
            project_id=project_id
        )

