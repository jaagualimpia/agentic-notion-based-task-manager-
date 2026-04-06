from src.integrations.notion.core import notion_client
from src.config import settings
import datetime

def get_last_tasks_checkpoint():
    week_span_start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

    record = notion_client.data_sources.query(
    data_source_id=settings.NOTION_DATA_SOURCE_ID,
    filter={
        "and": [
            {
                "property": "Fecha",
                "date": {"after": week_span_start_date }
            },
            {
                "property": "Tarea",
                "rich_text": {"contains": "Actividades"}
            },
        ]
    },
    sorts = [
        {
        "property": "Fecha",
        "direction": "descending"
        }
    ], 
    page_size = 1)

    return record["results"]