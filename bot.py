import telebot 
from telebot import types



bot = telebot.TeleBot("7270152731:AAEC0Let7smDFhQrtHaRqjMd55jGnZB8g4g")


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "ЕГОР ГЕЙ ХАХАХ")
    elif message.text == "q":
        bot.send_message(message.from_user.id, text="temp", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")



bot.polling(none_stop=True, interval=5)