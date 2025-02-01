from fastapi import HTTPException, APIRouter

from models.schemas import IMEISchema

from services.imei_services import get_imei_info
from services.validation_services import is_token_valid

imei_router = APIRouter()


@imei_router.post("/api/check-imei")
def check_imei(request: IMEISchema) -> dict:
    """
    Эндпоинт для получения информации об устройстве по номеру IMEI,
    требует передачи токена с запросом.
    """

    if not is_token_valid(request.token):
        raise HTTPException(
            status_code=403,
            detail="Неверный токен авторизации"
        )
    imei_info = get_imei_info(request.imei)
    if imei_info.get('error'):
        raise HTTPException(
            status_code=400,
            detail="Введен некорректный IMEI"
        )
    return {
        "imei": request.imei,
        "info_about_device": imei_info
    }
