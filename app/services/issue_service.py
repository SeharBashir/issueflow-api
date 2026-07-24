from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.issue_repository import IssueRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.issue import IssueCreate, IssueUpdate


class IssueService:

    def __init__(self):
        self.issue_repository = IssueRepository()
        self.project_repository = ProjectRepository()

    def create_issue(
        self,
        db: Session,
        issue: IssueCreate
    ):
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

    def get_issue_by_id(
        self,
        db: Session,
        issue_id: int
    ):
        issue = self.issue_repository.get_by_id(
            db=db,
            issue_id=issue_id
        )

        if issue is None:
            raise HTTPException(
                status_code=404,
                detail="Issue not found"
            )

        return issue

    def update_issue(
        self,
        db: Session,
        issue_id: int,
        issue_data: IssueUpdate
    ):
        issue = self.issue_repository.get_by_id(
            db=db,
            issue_id=issue_id
        )

        if issue is None:
            raise HTTPException(
                status_code=404,
                detail="Issue not found"
            )

        return self.issue_repository.update(
            db=db,
            issue=issue,
            issue_data=issue_data
        )

    def delete_issue(
        self,
        db: Session,
        issue_id: int
    ):
        issue = self.issue_repository.get_by_id(
            db=db,
            issue_id=issue_id
        )

        if issue is None:
            raise HTTPException(
                status_code=404,
                detail="Issue not found"
            )

        self.issue_repository.delete(
            db=db,
            issue=issue
        )

        return {
            "message": "Issue deleted successfully"
        }