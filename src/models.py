from sqlmodel import SQLModel, Table, Field
from pydantic import BaseModel
import datetime

class Projects(BaseModel):
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(nullable=False)
    description: str | None = Field(nullable=True)
    final_date: datetime.date = Field(nullable=True)
    repo_url: str = Field(nullable=True)
    access_token: str = Field(nullable=True)
    status: str = Field(nullable=False, default="ACTIVE")

class ProjectsModel(Projects, SQLModel, table = True):
    __tablename__ = "projects"