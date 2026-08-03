from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.enums import (
    IssuePriority,
    IssueStatus
)


class IssueCreate(BaseModel):
    title: str
    description: str | None = None
    priority: IssuePriority = IssuePriority.MEDIUM
    project_id: int


class IssueUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: IssueStatus | None = None
    priority: IssuePriority | None = None


class IssueResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: IssueStatus
    priority: IssuePriority
    project_id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True
    )