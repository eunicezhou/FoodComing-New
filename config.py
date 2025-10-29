from dotenv import load_dotenv
import os

# 讀取 .env
env = os.environ.get("ENVIRONMENT", "local")  # 預設 dev
load_dotenv(f".env.{env}")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    TESTING = os.getenv("TESTING") == "True"
    WTF_CSRF_ENABLED = os.getenv("WTF_CSRF_ENABLED") == "True"
    SERVER_NAME = os.getenv("SERVER_NAME")

    # sqlalchemy engine setting
    SQLALCHEMY_DATABASE_URI = f"""postgresql://{os.getenv("SQLALCHEMY_USERNAME")}:
                               {os.getenv("SQLALCHEMY_PASSWORD")}@127.0.0.1:5432/{os.getenv("SQLALCHEMY_DB")}"""
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": os.getenv("SQLALCHEMY_POOL_PRE_PING"),
        "pool_recycle": os.getenv("SQLALCHEMY_POOL_RECYCLE"),
        'pool_timeout': os.getenv("SQLALCHEMY_POOL_TIMEOUT"),
        'pool_size': os.getenv("SQLALCHEMY_POOL_SIZE"),
        'max_overflow': os.getenv("SQLALCHEMY_MAX_OVERFLOW"),
    }

config = Config()