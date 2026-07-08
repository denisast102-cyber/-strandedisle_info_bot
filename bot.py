import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "👋 Привет!\n\nДобро пожаловать в бота сервера Stranded Isle!"
    )

print("Бот запущен!")
bot.infinity_polling(skip_pending=True)
