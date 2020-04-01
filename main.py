from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)


# instantiate the Flask app
app = Flask(__name__)


@app.route('{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and convert into telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message.id

    # encoding text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()

    # for debugging purposes only
    print("got text message: ", text)

    # welcome message from the bot
    if text == "/start":
        # print welcome message
        bot_welcome = """Welcome to jharkhand covid 19 bot"""

        # send the welcome message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

    else:
        try:
            alt_welcome = """processing your reques"""
            bot.sendMessage(chat_id=chat_id, text=alt_welcome, reply_to_message_id=msg_id)
        except Exception:
            bot.sendMessage(chat_id=chat_id, text="There was a problem in your message",
                            reply_to_message_id=msg_id)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"


@app.route('/')
def index():
   return '.'
