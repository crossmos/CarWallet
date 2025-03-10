from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiV1Prefix(BaseModel):
    prefix: str = '/v1'
    users: str = '/users'
    transports: str = '/transports'
    fuel_losses: str = '/fuel_losses'
    repair_losses: str = '/repair_losses'
    spare_losses: str = '/spare_losses'
    supplie_losses: str = '/supplie_losses'


class ApiPrefix(BaseModel):
    prefix: str = '/api'
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseSettings):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = True
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


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
