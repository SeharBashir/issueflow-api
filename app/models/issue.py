from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.database.connection import Base


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(Text, nullable=True)

    status = Column(
        String(50),
        default="open",
        nullable=False
    )

    priority = Column(
        String(50),
        default="medium",
        nullable=False
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )