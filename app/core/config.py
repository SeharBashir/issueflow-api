from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "IssueFlow API"
    database_url: str = "sqlite:///./issueflow.db"
    debug: bool = False

    secret_key: str = "changeme-generate-a-real-secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()