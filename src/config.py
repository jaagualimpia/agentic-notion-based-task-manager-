from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str = Field(description="Database url for the project")
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

settings = Settings()