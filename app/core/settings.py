from pydantic_settings import BaseSettings
from enum import Enum 

from app.utils.env import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_DAYS

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
    ACCESS_TOKEN_EXPIRE_DAYS: int = ACCESS_TOKEN_EXPIRE_DAYS
    # CELERY_BROKER_URL: str = "amqp://rabbit:password@localhost:5672"
    # CELERY_BACKEND_URL: str = "redis://localhost:6379/0"

config: Config = Config()
