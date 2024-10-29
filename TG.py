import telebot
from telebot import types
from loguru import logger


bot = telebot.TeleBot('7307537829:AAExktbYOlVGL0WiMLI47K9VCL-LVEX0x9Y')
logger.success('Экземпляр бота создан')
m = types.Message
msg_chat_id='Антон'


@bot.message_handler(["start"])
def start(msg:m):
    logger.info(f'Пользователь {msg_chat_id} нажал команду "старт"')
    bot.send_message(msg.chat.id, "пройди опрос-/letsgo")



bot.infinity_polling()
