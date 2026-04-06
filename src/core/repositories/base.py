from typing import Generic, TypeVar, Type, Any
from sqlmodel import SQLModel, Session, select

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def find_one(self, id: Any) -> T | None:
        return self.session.get(self.model, id)

    def find_many(self, **filters) -> list[T]:
        statement = select(self.model)
        for key, value in filters.items():
            statement = statement.where(getattr(self.model, key) == value)
        return self.session.exec(statement).all()

    def create(self, obj: T) -> T:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def update(self, id: Any, data: dict) -> T | None:
        obj = self.find_one(id)
        if obj is None:
            return None
        for key, value in data.items():
            setattr(obj, key, value)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, id: Any) -> bool:
        obj = self.find_one(id)
        if obj is None:
            return False
        self.session.delete(obj)
        self.session.commit()
        return True
