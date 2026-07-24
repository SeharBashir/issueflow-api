from sqlalchemy.orm import Session

from app.models.issue import Issue
from app.schemas.issue import IssueCreate, IssueUpdate


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

    def get_by_id(
        self,
        db: Session,
        issue_id: int
    ) -> Issue | None:

        return db.query(Issue).filter(
            Issue.id == issue_id
        ).first()

    def get_by_project_id(
        self,
        db: Session,
        project_id: int
    ) -> list[Issue]:

        return db.query(Issue).filter(
            Issue.project_id == project_id
        ).all()

    def update(
        self,
        db: Session,
        issue: Issue,
        issue_data: IssueUpdate
    ) -> Issue:

        update_data = issue_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(issue, field, value)

        db.commit()
        db.refresh(issue)

        return issue

    def delete(
        self,
        db: Session,
        issue: Issue
    ) -> None:

        db.delete(issue)
        db.commit()