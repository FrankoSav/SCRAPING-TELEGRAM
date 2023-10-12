import re
import logging
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_TOKEN = ' '

CANAL_ID_1 = 
CANAL_ID_2 = 
CANAL_ID_3 = 

CANAL_DESTINO_ID = ' '

EMAIL_PASSWORD_REGEX = r'(\S+:\S+)'

bot = Bot(token=BOT_TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def procesar_enviar_correos_contraseñas(update, context):
    text = update.message.text
    matches = re.findall(EMAIL_PASSWORD_REGEX, text)
    for match in matches:
        correo_contraseña = match
        mensaje_a_enviar = '\n'.join(correo_contraseña)
        bot.send_message(chat_id=CANAL_DESTINO_ID, text=mensaje_a_enviar)
        logger.info(f"Correo y contraseña enviados a {CANAL_DESTINO_ID}: {mensaje_a_enviar}")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & Filters.regex(EMAIL_PASSWORD_REGEX), procesar_enviar_correos_contraseñas))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()