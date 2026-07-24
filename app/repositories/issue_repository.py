
from sqlalchemy.orm import Session

from app.models.issue import Issue
from app.schemas.issue import IssueCreate


class IssueRepository:

    def create(
        self,
        db: Session,
        issue_data: IssueCreate
    ) -> Issue:

        issue = Issue(
            title=issue_data.title,
            description=issue_data.description,
            priority=issue_data.priority,
            project_id=issue_data.project_id
        )

        db.add(issue)
        db.commit()
        db.refresh(issue)

        return issue

    def get_all(
        self,
        db: Session
    ) -> list[Issue]:

        return db.query(Issue).all()

    def get_by_project_id(
        self,
        db: Session,
        project_id: int
    ) -> list[Issue]:

        return db.query(Issue).filter(
            Issue.project_id == project_id
        ).all()

