
from src.core.db import get_db_session
from src.projects.repositories.projects_repository import ProjectRepository
from src.projects.services.projects_service import ProjectsService


def get_project_service():
    return ProjectsService(ProjectRepository(get_db_session()))