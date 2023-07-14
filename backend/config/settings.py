from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.utils import get_envfile


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=get_envfile(), env_file_encoding="utf-8")
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "user"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "database_name"
    SECRET_KEY: str = "my_precious_secret_key"
    DEBUG: bool = False


settings = Settings()
