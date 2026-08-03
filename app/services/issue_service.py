from sqlalchemy.orm import Session

from app.repositories.issue_repository import IssueRepository
from app.repositories.project_repository import ProjectRepository
from app.schemas.issue import IssueCreate, IssueUpdate
from app.core.exceptions import NotFoundException, BadRequestException


class IssueService:

    def __init__(self):
        self.issue_repository = IssueRepository()
        self.project_repository = ProjectRepository()

    def _get_project_or_404(
        self,
        db: Session,
        project_id: int
    ):
        project = self.project_repository.get_by_id(
            db=db,
            project_id=project_id
        )

        if project is None:
            raise NotFoundException("Project", project_id)

        return project

    def _get_issue_or_404(
        self,
        db: Session,
        issue_id: int
    ):
        issue = self.issue_repository.get_by_id(
            db=db,
            issue_id=issue_id
        )

        if issue is None:
            raise NotFoundException("Issue", issue_id)

        return issue

    def create_issue(
        self,
        db: Session,
        issue: IssueCreate
    ):
        self._get_project_or_404(
            db=db,
            project_id=issue.project_id
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
        self._get_project_or_404(
            db=db,
            project_id=project_id
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
        return self._get_issue_or_404(
            db=db,
            issue_id=issue_id
        )

    def validate_status_transition(
        self,
        current_status: str,
        new_status: str
    ):
        allowed_transitions = {
            "open": ["in_progress"],
            "in_progress": ["resolved"],
            "resolved": ["closed", "in_progress"],
            "closed": []
        }

        if new_status not in allowed_transitions[current_status]:
            raise BadRequestException(
                detail=(
                    f"Cannot change status from "
                    f"{current_status} to {new_status}"
                )
            )

    def update_issue(
        self,
        db: Session,
        issue_id: int,
        issue_data: IssueUpdate
    ):
        issue = self._get_issue_or_404(
            db=db,
            issue_id=issue_id
        )

        if issue_data.status is not None:

            self.validate_status_transition(
                current_status=issue.status,
                new_status=issue_data.status.value
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
        issue = self._get_issue_or_404(
            db=db,
            issue_id=issue_id
        )

        self.issue_repository.delete(
            db=db,
            issue=issue
        )

        return {
            "message": "Issue deleted successfully"
        }