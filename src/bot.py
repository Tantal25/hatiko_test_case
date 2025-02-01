from telegram import Update
from telegram.ext import (
    CommandHandler, ApplicationBuilder, ContextTypes, MessageHandler, filters
)

from services.imei_services import get_imei_info
from services.validation_services import is_user_in_whitelist
from settings import SettingsConfig


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Стартовая функция в боте, делает запрос на доступ пользователя к сервису.
    """

    if not is_user_in_whitelist(update.effective_user.id):
        await update.message.reply_text(
            'Вам не разрешен доступ к боту, '
            'зарегистрируйтесь и укажите свой Telegram ID в аккаунте'
        )
        return
    await update.message.reply_text('Введите IMEI устройства для проверки')


async def check_imei(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Функция проверяющая устройство по введенному IMEI 
    в сервисе https://imeicheck.net/
    """

    imei = update.message.text
    imei_info = get_imei_info(imei)
    if imei_info.get('error'):
        await update.message.reply_text(imei_info['error'])
        await update.message.reply_text('Введите корректный IMEI устройства')
        return
    await update.message.reply_text(imei_info)
    await update.message.reply_text('Введите IMEI устройства')


def main():
    app = ApplicationBuilder().token(
        SettingsConfig.IMEI_CHECK_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, check_imei)
    )
    app.run_polling()


if __name__ == '__main__':
    main()
