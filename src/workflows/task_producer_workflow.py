from langchain_openai.chat_models import ChatOpenAI

from src.integrations.notion.services.notion_blocks_service import travel_activities_root_block
from src.integrations.notion.services.notion_data_source_service import get_last_tasks_checkpoint

def run_aware_task_planner():
    activities_task_pool_block = get_last_tasks_checkpoint()
    activities_in_the_task_pool_block = travel_activities_root_block(activities_task_pool_block) 
    
    return activities_in_the_task_pool_block