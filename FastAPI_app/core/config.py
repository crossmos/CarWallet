from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseSettings):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = True
    pool_size: int = 50
    max_overflow: int = 10


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 8080


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env-template', '.env',),
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='APP_CONFIG__',
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
print(settings.db.url)