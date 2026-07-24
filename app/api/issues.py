
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.issue import IssueCreate
from app.services.issue_service import IssueService


router = APIRouter(
    prefix="/issues",
    tags=["Issues"]
)


issue_service = IssueService()


@router.post("/", status_code=201)
def create_issue(
    issue: IssueCreate,
    db: Session = Depends(get_db)
):
    return issue_service.create_issue(
        db=db,
        issue=issue
    )


@router.get("/")
def get_issues(
    db: Session = Depends(get_db)
):
    return issue_service.get_all_issues(db)


@router.get("/project/{project_id}")
def get_project_issues(
    project_id: int,
    db: Session = Depends(get_db)
):
    return issue_service.get_issues_by_project(
        db=db,
        project_id=project_id
    )

