from fastapi import HTTPException, APIRouter

from sqlalchemy.exc import IntegrityError

from models.db import Session, User
from models.schemas import UserSchema
from services.db_services import create_token_in_db, create_user_in_db


user_router = APIRouter()


@user_router.post("/api/create_user")
def create_user(user: UserSchema) -> dict:
    """
    Эндпоинт для создания пользователя и получения токена для него,
    опционально может быть добавлен Telegram ID.
    """
    session = Session()
    try:
        new_user = create_user_in_db(user, session)
        # Обновляем  БД, для доступа к пользователю
        session.flush()
        token = create_token_in_db(new_user, session)
        session.commit()
        return {
            'username': new_user.username,
            'access_token': token.token
        }
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Ошибка при создании пользователя - {e.args}"
        )
    finally:
        session.close()


@user_router.post("/api/get_token")
def get_token(user: UserSchema):
    """Эндпоинт для получения токена, по username пользователя."""
    session = Session()
    user = session.query(User).filter_by(username=user.username).first()
    return {"access_token": user.token.token}
