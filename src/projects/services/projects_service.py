from src.core.services.base import BaseService
from src.models import ProjectsModel

class ProjectsService(BaseService[ProjectsModel]):
    def __init__(self, repository):
        super().__init__(repository)