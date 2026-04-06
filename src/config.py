from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str = Field(description="Database url for the project")
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    NOTION_INTEGRATION_KEY: str
    NOTION_DATA_SOURCE_ID: str
    OPENAI_API_KEY: str

settings = Settings()