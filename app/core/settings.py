from pydantic_settings import BaseSettings

from enum import Enum 

SECRET_KEY = "4f400364dc36a8bd1895874efe0b7469f29e7ed863ec903c5f10d8e82dc7c4d9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*7

class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    # REDIS_URL: RedisDsn = "redis://localhost:6379/7"
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0
    SECRET_KEY: str = SECRET_KEY
    ALGORITHM: str = ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES: int = ACCESS_TOKEN_EXPIRE_MINUTES
    # CELERY_BROKER_URL: str = "amqp://rabbit:password@localhost:5672"
    # CELERY_BACKEND_URL: str = "redis://localhost:6379/0"


config: Config = Config()
