from src.config import settings
from notion_client import Client

notion_client = Client(auth=settings.NOTION_INTEGRATION_KEY)