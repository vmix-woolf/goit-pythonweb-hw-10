from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str

    # JWT auth
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # SMTP
    smtp_host: str
    smtp_port: int
    smtp_user: str
    smtp_password: str
    mail_from: str

    # Cloudinary
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    app_url: str

    model_config = {
        "env_file": ".env",
        "extra": "forbid"
    }


settings = Settings()

