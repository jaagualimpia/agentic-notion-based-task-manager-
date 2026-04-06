from src.core.repositories.base import BaseRepository
from src.models import ProjectsModel

class ProjectRepository(BaseRepository[ProjectsModel]):
    def __init__(self, session):
        super().__init__(session, ProjectsModel)