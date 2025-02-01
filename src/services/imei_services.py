from json import loads

import requests

from services.validation_services import is_imei_valid
from settings import SettingsConfig


def get_imei_info(imei: str) -> str:
    """
    Функция для проверки устройства по IMEI,
    через сервис https://imeicheck.net/.
    """
    # Передаем в заголовке TOKEN для доступа к сервису
    headers = {
        "Authorization":
        SettingsConfig.CHECK_IMEI_API_TOKEN
    }

    # В теле передаем IMEI и номер сервиса,
    # который проверяет устройства по нему
    payload = {
        "deviceId": imei,
        "serviceId": 12
    }

    response = requests.post(
        SettingsConfig.CHECK_IMEI_API_URL,
        json=payload,
        headers=headers
    )

    dict_response_data = loads(response.text)
    if is_imei_valid(dict_response_data):
        return dict_response_data
    return {"error": "Некорректный номер IMEI"}
