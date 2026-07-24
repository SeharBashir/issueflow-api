from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.issue import IssueCreate, IssueUpdate
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


@router.get("/{issue_id}")
def get_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    return issue_service.get_issue_by_id(
        db=db,
        issue_id=issue_id
    )


@router.put("/{issue_id}")
def update_issue(
    issue_id: int,
    issue_data: IssueUpdate,
    db: Session = Depends(get_db)
):
    return issue_service.update_issue(
        db=db,
        issue_id=issue_id,
        issue_data=issue_data
    )


@router.delete("/{issue_id}")
def delete_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    return issue_service.delete_issue(
        db=db,
        issue_id=issue_id
    )