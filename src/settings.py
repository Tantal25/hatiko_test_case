import os

from dotenv import load_dotenv


load_dotenv()


class SettingsConfig:
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///database.db')
    IMEI_CHECK_BOT_TOKEN = os.getenv('IMEI_CHECK_BOT_TOKEN')
    CHECK_IMEI_API_URL = os.getenv('CHECK_IMEI_API_URL')
    CHECK_IMEI_API_TOKEN = os.getenv('CHECK_IMEI_API_TOKEN')
