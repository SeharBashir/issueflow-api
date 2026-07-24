from pydantic import BaseModel


class IssueCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "medium"
    project_id: int


class IssueUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None