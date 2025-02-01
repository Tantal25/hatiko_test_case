from secrets import token_hex

from models.db import Token, Session, User
from models.schemas import UserSchema


def create_user_in_db(
        user: UserSchema,
        session: Session,
) -> User:
    """Функция для создания Пользователя в БД."""
    if user.telegram_id:
        new_user = User(username=user.username, telegram_id=user.telegram_id)
    else:
        new_user = User(username=user.username)
    session.add(new_user)
    return new_user


def create_token_in_db(user: User, session: Session) -> str:
    """Функция для создания Токена связанного с пользователем в БД."""
    new_token = Token(token=token_hex(), token_id=user.user_id)
    session.add(new_token)
    return new_token
