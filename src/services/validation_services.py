from models.db import Session, Token, User


def is_token_valid(token: str) -> bool:
    """Функция для проверки существования токена."""
    session = Session()
    result = session.query(Token).filter_by(token=token).first()
    session.close
    return result is not None


def is_imei_valid(response: str) -> bool:
    """Функция проверяет, ответ от сервиса
    https://imeicheck.net/, валиден ли IMEI."""
    if response.get('errors'):
        return False
    return True


def is_user_in_whitelist(telegram_id: int) -> bool:
    """
    Функция для проверки присутствует ли пользователь с указанным
    Telegram ID в списке зарегистрированных.
    """
    session = Session()
    allowed_user = (
        session.query(User).filter_by(telegram_id=telegram_id).first()
    )
    session.close()
    return allowed_user is not None
