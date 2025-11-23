from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

# Налаштування сервера пошти
mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.smtp_user,
    MAIL_PASSWORD=settings.smtp_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.smtp_port,
    MAIL_SERVER=settings.smtp_host,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)

fm = FastMail(mail_config)


async def send_verification_email(email: str, token: str):
    """
    Надсилає лист для підтвердження email користувача.
    """
    verify_url = f"{settings.app_url}/auth/verify?token={token}"

    message = MessageSchema(
        subject="Verify your email",
        recipients=[email],
        body=f"Для підтвердження вашого акаунта перейдіть за посиланням:\n{verify_url}",
        subtype="plain",
    )

    await fm.send_message(message)
