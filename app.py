from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from functools import wraps


# Stages
FIRST, SECOND, THIRD = range(3)

# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = range(9)


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func

def start(update, context):
    fname = update.message.from_user.first_name

    # Build InlineKeyboard
    keyboard1 = [InlineKeyboardButton("सरकार द्वारा प्रशंसित सभी योजनाओं को जानें", callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton("Covid 19 के बारे में जानकारी प्राप्त करें", callback_data=str(TWO))]
    keyboard3 = [InlineKeyboardButton("किसी भी समस्या के बारे में सूचित करें", callback_data=str(THREE))]
        
    # create reply markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])

    # send message with text and appended inline keyboarde
    update.message.reply_text(
        "नमस्कार {}, Jharkhand Covid19 bot आपका स्वागत करता है।\n\nनीचे दिए गए विकल्पों में से एक का चयन करें".format(fname),
        reply_markup=reply_markup
    )
    # tell ConversationHandler that we're in state 'FIRST' now
    return FIRST

def start_over(update, context):
    # Get callback query from update
    query = update.callback_query

    # answering callback query
    query.answer()
    # Build InlineKeyboard
    keyboard1 = [InlineKeyboardButton("सरकार द्वारा प्रशंसित सभी योजनाओं को जानें", callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton("Covid 19 के बारे में जानकारी प्राप्त करें", callback_data=str(TWO))]
    keyboard3 = [InlineKeyboardButton("किसी भी समस्या के बारे में सूचित करें", callback_data=str(THREE))]
    # create reply markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3])

    # send message with text and appended inline keyboarde
    query.edit_message_text(
        "नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    # tell ConversationHandler that we're in state 'FIRST' now
    return FIRST


def one(update, context):
    """show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # build inline keyboard
    keyboard1 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton("समाप्त करें", callback_data=str(TWO))]
    #create reply markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])
    query.edit_message_text(
        "झारखंड सरकार सभी राशन कार्ड धारकों को दो महीने के लिए मुफ्त राशन प्रदान करेगी\n\nजिन लोगों ने राशन कार्ड के लिए आवेदन किया है, लेकिन उन्हें कार्ड मिलना बाकी है, उन्हें भी मुफ्त चावल दिया जाएगा\n ",
        reply_markup=reply_markup
    )
    return SECOND

def two(update, context):
    """show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # build keyboard
    keyboard1 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton("समाप्त करें", callback_data=str(TWO))]
    # create reply markup
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2])
    query.edit_message_text(
        "Will update this section",
        reply_markup=reply_markup
    )
    return SECOND


def three(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard1 = [InlineKeyboardButton("भोजन और आवश्यक वस्तुएँ ना मिलना", callback_data=str(ONE))]
    keyboard2 = [InlineKeyboardButton("चिकित्सा सुविधा नहीं मिलने की समस्या", callback_data=str(TWO))]
    keyboard3 = [InlineKeyboardButton("वाहन के लिए e-pass जारी करना", callback_data=str(THREE))]
    keyboard4 = [InlineKeyboardButton("आश्रय की समस्या", callback_data=str(FOUR))]
    keyboard5 = [InlineKeyboardButton("झारखंड में फंसे", callback_data=str(FIVE))]
    keyboard6 = [InlineKeyboardButton("झारखंड के बाहर फंसे", callback_data=str(SIX))]
    keyboard7 = [InlineKeyboardButton("अन्य", callback_data=str(SEVEN))]
    keyboard8 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(EIGHT))]
    keyboard9 = [InlineKeyboardButton("समाप्त करें", callback_data=str(NINE))]
    
    reply_markup = InlineKeyboardMarkup([keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6, keyboard7, keyboard8, keyboard9])
    query.edit_message_text(
        text="नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    
    return FIRST

def four(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # create keyboards
    keyboard8 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(EIGHT))]
    keyboard9 = [InlineKeyboardButton("समाप्त करें", callback_data=str(NINE))]
    # create markup
    reply_markup = InlineKeyboardMarkup([keyboard8, keyboard9])
    query.edit_message_text(
        text="नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    return FIRST

def five(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # create keyboards
    keyboard8 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(EIGHT))]
    keyboard9 = [InlineKeyboardButton("समाप्त करें", callback_data=str(NINE))]
    # create markup
    reply_markup = InlineKeyboardMarkup([keyboard8, keyboard9])
    query.edit_message_text(
        text="नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    return FIRST

def six(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # create keyboards
    keyboard8 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(EIGHT))]
    keyboard9 = [InlineKeyboardButton("समाप्त करें", callback_data=str(NINE))]
    # create markup
    reply_markup = InlineKeyboardMarkup([keyboard8, keyboard9])
    query.edit_message_text(
        text="नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    return FIRST

def seven(update, context):
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    # create keyboards
    keyboard8 = [InlineKeyboardButton("फिर से शुरू करें", callback_data=str(EIGHT))]
    keyboard9 = [InlineKeyboardButton("समाप्त करें", callback_data=str(NINE))]
    # create markup
    reply_markup = InlineKeyboardMarkup([keyboard8, keyboard9])
    query.edit_message_text(
        text="नीचे दिए गए विकल्पों में से एक का चयन करें",
        reply_markup=reply_markup
    )
    return FIRST

def end(update, context):
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="मेरे साथ चैट करने के लिए धन्यवाद।\n\nमुझसे फिर से बात करने के लिए टाइप करें /start\n\nघर में रहे, सुरक्षित रहे।"
    )
    return ConversationHandler.END

def keyboard_query_response(update, context):
    update.message.reply_text(
        "मेरे साथ चैट करने के लिए केवल सूचीबद्ध विकल्पों का उपयोग करें"
    )


def main():
    updater = Updater(token="1179864522:AAFA2-YjGNpFzHTKpMYZA3z4Jw5Y8KeMBLQ", use_context=True)
    dispatcher = updater.dispatcher
    print("Bot started")

    # Setup conversation handler with states FIRST and SECOND
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(command='start', callback=start)],
        states={
            FIRST: [CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                    CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                    CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                    CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                    CallbackQueryHandler(five, pattern='^' + str(FIVE) + '$'),
                    CallbackQueryHandler(six, pattern='^' + str(SIX) + '$'),
                    CallbackQueryHandler(seven, pattern='^' + str(SEVEN) + '$'),
                    CallbackQueryHandler(start_over, pattern='^' + str(EIGHT) + '$'),
                    CallbackQueryHandler(end, pattern='^' + str(NINE) + '$')],
            SECOND: [CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                     CallbackQueryHandler(end, pattern='^' + str(TWO) + '$')]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    
    # set up MessageHandler to reply to random messages
    random_response_handler = MessageHandler(filters=Filters.text, callback=keyboard_query_response)
    # add command handler to dispatcher
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(random_response_handler)

    # start the bot
    updater.start_polling()

    # run the bot until pressed ctrl+c
    updater.idle()


if __name__ == "__main__":
    main()