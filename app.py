from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.message.reply_text("I'm a bot. Nice to meet you")

def convert_uppercase(bot, update):
    update.message.reply_text(update.message.text.upper())

def main():
    updater = Updater(token="1179864522:AAFA2-YjGNpFzHTKpMYZA3z4Jw5Y8KeMBLQ")
    dispatcher = updater.dispatcher
    print("Bot started")

    # add command handler to dispatcher
    start_handler = CommandHandler(command='start', callback=start)
    upper_case = MessageHandler(filters=Filters.text, callback=convert_uppercase)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(upper_case)

    # start the bot
    updater.start_polling()

    # run the bot until pressed ctrl+c
    updater.idle()


if __name__ == "__main__":
    main()