from src.agents.schemas.dtos.task_producer_dto import TaskDto
from src.models import ProjectsModel


def parse_projects_for_prompt(projects: list[ProjectsModel]):
    FIELDS_TO_OMIT = ["id", "access_token", "repo_url"]
    parsed_projects = ""
    
    filtered_projects = [project.model_dump(mode="json", exclude=FIELDS_TO_OMIT) for project in projects]

    for project in filtered_projects:
        parsed_projects += f"\n"
        for key, value in project.items():
            parsed_projects += f"- {key}: {value} \n"

    return parsed_projects

def parse_tasks_for_prompt(tasks: list[TaskDto]):
    FIELDS_TO_OMIT = []
    parsed_tasks = ""
    
    filtered_tasks = [task.model_dump(mode="json", exclude=FIELDS_TO_OMIT) for task in tasks]

    for task in filtered_tasks:
        parsed_tasks += f"\n"
        for key, value in task.items():
            parsed_tasks += f"- {key}: {value} \n"

    return parsed_tasks