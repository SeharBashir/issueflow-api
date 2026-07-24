from pydantic import BaseModel


class IssueCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "medium"
    project_id: int