from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from botspace.credentials import bot_token, URL

global bot
global TOKEN
TOKEN = bot_token
bot = telebot.TeleBot(token=TOKEN)


# instantiate the Flask app
app = Flask(__name__)


def gen_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("सरकार द्वारा प्रशंसित सभी योजनाओं को जानें", callback_data="cb_opt1"),
                InlineKeyboardButton("Covid 19 के बारे में जानकारी प्राप्त करें", callback_data="cb_opt2"),
                InlineKeyboardButton("किसी भी समस्या के बारे में सूचित करें", callback_data="cb_opt3")
    )
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                text='नमस्कार {}, jharkhandCovid19 bot आपका स्वागत करता है\n\nनीचे दिए गए विकल्पों में से एक का चयन करें'.format(message.from_user.first_name), reply_markup=gen_markup())
    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_opt1":
        bot.answer_callback_query(call.id, "You chose option 1")
    elif call.data == "cb_opt2":
        bot.answer_callback_query(call.id, "You chose option 2")
    elif call.data == "cb_opt3":
        bot.answer_callback_query(call.id, "You chose option 3")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Choose preferred option",
                    reply_markup=gen_markup())


@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(
        request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'
