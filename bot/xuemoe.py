import telebot

from birsha import get_dollar

bot = telebot.TeleBot("948151536:AAERhTU0PULOXjotgpTZdp9uZ8xOaZF9N0Y")

from telebot import  types

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ну погнали, ебана в рот')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text =="привет" or message.text =="Здравствуйте"or message.text =="здравствуйте":
        bot.send_message(message.from_user.id, "Ну привет, хуила. Чо почем бакс хочешь знать?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Тебе уже ничего не поможет, уебище")
    elif message.text == "Да" or message.text == "Го":
        keyboard = types.InlineKeyboardMarkup()
        key_dollar = types.InlineKeyboardButton(text='USD', callback_data='key_dollar')
        keyboard.add(key_dollar)
        key_evro = types.InlineKeyboardButton(text='EUR', callback_data='key_evro')
        keyboard.add(key_evro)
        key_funt = types.InlineKeyboardButton(text='GBP', callback_data='key_funt')
        keyboard.add(key_funt)
        key_novzeland_dollar = types.InlineKeyboardButton(text='NZD', callback_data='key_novzeland_dollar')
        keyboard.add(key_novzeland_dollar)
        key_avstr_dollar = types.InlineKeyboardButton(text='AUD', callback_data='key_avstr_dollar')
        keyboard.add(key_avstr_dollar)
        key_japan_yen = types.InlineKeyboardButton(text='JPY', callback_data='key_japan_yen')
        keyboard.add(key_japan_yen)
        bot.send_message(message.from_user.id, text='Выбирай хуле', reply_markup=keyboard)
    elif message.text == "Пока" or message.text == "пока" or message.text == "покеда":
            bot.send_message(message.from_user.id, "Ну и пошел на хуй!")
    elif message.text == "Спасибо" or message.text == "спасибо" or message.text == "От души брат":
            bot.send_message(message.from_user.id, "Должен будешь")
    else:
        bot.send_message(message.from_user.id, "Вежливее будь, нихуя же не понятно, поздоровайся сначала")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "key_dollar":
        bot.send_message(call.message.chat.id, get_dollar())
    elif call.data == "key_evro":
        bot.send_message(call.message.chat.id, 'key_evro')
    elif call.data == "key_funt":
        bot.send_message(call.message.chat.id, 'key_funt')
    elif call.data == "key_novzeland_dollar":
        bot.send_message(call.message.chat.id, 'key_novzeland_dollar')
    elif call.data == "key_avstr_dollar":
        bot.send_message(call.message.chat.id, 'key_avstr_dollar')
    elif call.data == "key_japan_yen":
        bot.send_message(call.message.chat.id, 'key_japan_yen')

bot.polling(none_stop=True, interval=0)
