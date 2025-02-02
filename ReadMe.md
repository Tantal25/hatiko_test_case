## Запуск приложения
- Клонировать репозиторий
`git clone git@github.com:Tantal25/hatiko_test_case.git`

- Установить и активировать виртуальное окружение
`python -m venv venv`
Windows: `source venv/Scripts/activate`
Linux: `source venv/bin/activate`

- Установить зависимости
`pip install -r requirements.txt`

- Создать в корневой директории проекта файл .env
IMEI_CHECK_BOT_TOKEN=<Токен телеграм бота>
CHECK_IMEI_API_URL=https://api.imeicheck.net/v1/checks
CHECK_IMEI_API_TOKEN=<Токен для внешнего API проверки IMEI>

- Запуск API для проверки
    1. Зайти в корневую директорию
    2. Либо запустить файл main.py напрямую либо выполнить в терминале команду `python src/main.py`


- Запуск бота для проекта
    1. Через API создать пользователя со своим TelegramID, чтобы занести его в Whitelist (иммитируем регистрацию в сервисе)
    2. Зайти в корневую директорию
    3. Либо запустить файл bot.py напрямую либо выполнить в терминале команду `python src/bot.py`
    4. В Telegram найти бота - @new_imei_checker_bot
    6. Запустить через команду /start (Если TelegramID не будет в базе данных, то вылетит ошибка)
    5. После получения сообщения - введите IMEI устройства для проверки, можно вводить разные подряд один за другим


Выгрузил одну из баз данных в репозиторий, там представлен пользователь с данными:
{
  "username": "John",
  "access_token": "754d1ea63db0ba6d2a86f442995b9c0b4e4b35f5150ea5c8e1927761b5a70e36"
}



## Эндпоинты
1. Эндпоинт для создания пользователя - `http://127.0.0.1:8000/api/create_user`
Пример запроса без telegram_id:
```
{
    "username": "John2"
}
```

Пример запроса с telegram_id:
```
{
    "username": "John2",
    "telegram_id": <сюда вставить Telegram ID для работы>
}
```

2. Эндпоинт для получения тоекна = `http://127.0.0.1:8000/api/get_token`
Пример запроса:
```
{
    "username": "John2"
}
```

3. Эндпоинт для проверки устройства по IMEI - `http://127.0.0.1:8000/api/check-imei`
Пример запроса, указан токен из уже существующей записи в БД:
```
{
  "imei": "350805486317462",
  "token": "754d1ea63db0ba6d2a86f442995b9c0b4e4b35f5150ea5c8e1927761b5a70e36"
}
```
