import datetime

from langchain_openai.chat_models import ChatOpenAI

from src.agents.schemas.dtos.task_producer_dto import TaskDto
from src.agents.prompts.task_producer_workflow_prompts import TASK_PRODUCER_WORKFLOW_BASE_PROMPT
from src.agents.parsers.task_produce_workflow_parsers import parse_projects_for_prompt, parse_tasks_for_prompt
from src.projects.dependencies import get_project_service
from src.integrations.notion.services.notion_blocks_service import travel_activities_root_block
from src.integrations.notion.services.notion_data_source_service import get_last_tasks_checkpoint
from src.config import settings


def run_aware_task_planner():
    projects_service = get_project_service()
    llm = ChatOpenAI(model="gpt-5.4", api_key=settings.OPENAI_API_KEY)

    tasks_pool_notion_block = get_last_tasks_checkpoint()
    tasks_pool = travel_activities_root_block(tasks_pool_notion_block)

    projects = projects_service.get_all()

    tasks = [TaskDto(**task) for task in tasks_pool]

    projects_prompt = parse_projects_for_prompt(projects)
    tasks_prompt = parse_tasks_for_prompt(tasks)

    messages = TASK_PRODUCER_WORKFLOW_BASE_PROMPT.invoke({
        "projects_context": projects_prompt,
        "tasks_context": tasks_prompt,
        "current_date": datetime.datetime.now().strftime("%Y-%m-%d")
    })

    response = llm.invoke(messages)

    print(response.content)    
 
    # return activities_in_the_task_pool_block