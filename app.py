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


def gen_markup2():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("भोजन और आवश्यक वस्तुएँ ना मिलना", callback_data="cb_food"),
               InlineKeyboardButton("चिकित्सा सुविधा नहीं मिलने की समस्या", callback_data="cb_healthcare"),
               InlineKeyboardButton("वाहन के लिए e-pass जारी करना", callback_data="cb_e-pass"),
               InlineKeyboardButton("आश्रय की समस्या", callback_data="cb_shelter"),
               InlineKeyboardButton("झारखंड में फंसे", callback_data="cb_in_migrant"),
               InlineKeyboardButton("झारखंड के बाहर फंसे", callback_data="cb_out_migrant"),
               InlineKeyboardButton("अन्य", callback_data="cb_others")
               )
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 text='नमस्कार {}, jharkhandCovid19 bot आपका स्वागत करता है\n\nनीचे दिए गए विकल्पों में से एक का चयन करें'.format(message.from_user.first_name), reply_markup=gen_markup()
                 )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_opt1":
        bot.answer_callback_query(call.id, "You chose option 1")
    elif call.data == "cb_opt2":
        bot.answer_callback_query(call.id, "You chose option 2")
    elif call.data == "cb_opt3":
        bot.answer_callback_query(call.id, "किसी भी समस्या के बारे में सूचित करें")
        share_information(message="cb_opt3")
    elif call.data == "cb_food":
        bot.answer_callback_query(call.id, "food")
    elif call.data == "cb_shelter":
        bot.answer_callback_query(call.id, "shelter")
    elif call.data == "cb_healthcare":
        bot.answer_callback_query(call.id, "healthcare")
    elif call.data == "cb_e-pass":
        bot.answer_callback_query(call.id, "e-pass")
    elif call.data == "cb_in_migrant":
        bot.answer_callback_query(call.id, "in-migrant")
    elif call.data == "cb_out_migrant":
        bot.answer_callback_query(call.id, "out-migrant")
    elif call.data == "cb_others":
        bot.answer_callback_query(call.id, "others")


@bot.message_handler(commands=['share_info'])
def share_information(message):
    if message == "cb_opt3":
        bot.reply_to(message, text="नीचे दिए गए विकल्पों में से एक का चयन करें",
                     reply_markup=gen_markup2())


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
