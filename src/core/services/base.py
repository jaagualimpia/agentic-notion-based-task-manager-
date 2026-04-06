from typing import Generic, TypeVar, Any
from sqlmodel import SQLModel
from src.core.repositories.base import BaseRepository

T = TypeVar("T", bound=SQLModel)


class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get_by_id(self, id: Any) -> T | None:
        return self.repository.find_one(id)

    def get_all(self, **filters) -> list[T]:
        return self.repository.find_many(**filters)

    def create(self, obj: T) -> T:
        return self.repository.create(obj)

    def update(self, id: Any, data: dict) -> T | None:
        return self.repository.update(id, data)

    def delete(self, id: Any) -> bool:
        return self.repository.delete(id)
