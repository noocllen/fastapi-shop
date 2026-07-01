from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list = [
        "htttp://localhost:5173",
        "htttp://localhost:3000",
        "htttp://127.0.0.1:5173",
        "htttp://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        env_file = ".env"

settings = Settings()
