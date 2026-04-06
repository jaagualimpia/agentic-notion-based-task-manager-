from pydantic import BaseModel


class TaskDto(BaseModel):
    task: str
    path: list[str]