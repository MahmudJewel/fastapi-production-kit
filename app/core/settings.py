from pydantic_settings import BaseSettings
from enum import Enum 
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

SECRET_KEY = "4f400364dc36a8bd1895874efe0b7469f29e7ed863ec903c5f10d8e82dc7c4d9"
REFRESH_SECRET_KEY = "b7f01fe0c8c0f182a048963d7eb05e177f3a893963c8eed58b16ce2fef7c50e5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*7 # 1day
REFRESH_TOKEN_EXPIRE_DAYS = 7 # 7 day

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = "http://127.0.0.1:8000/social/auth/google/callback"

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
