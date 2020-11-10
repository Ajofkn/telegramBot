import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import nasScrape2
import os
# Logging information on the terminal, just to check what's up
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Command for start. Gives a little helpful tip on how to use the bot.
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Use /stock <stock name> to find the information on the stock.')

# Command for the stock bot. It accepts the ticker as args[0], and then uses that ticker in the nasScrape2 file to recieve a formatted string of the data I want before replying it back to the user who initiated it. 
def stocks(update: Update, context: CallbackContext) ->None:
    try:
        tickerValue = context.args[0]
        tickerInfo = nasScrape2.ticker(tickerValue)
        update.message.reply_text(tickerInfo)

    except(IndexError, ValueError):
        update.message.send_message("Something went wrong.")



def main():
    apiToken = os.environ.get('TELEGRAMAPI')
    # Create an updater, and throw in my token in it
    updater = Updater(token=apiToken, use_context=True)

    # Dispatcher to register handlers/commands
    dispatcher = updater.dispatcher

    # Commands available to the bot thus far
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stock", stocks))

    # Starts the bot, and doesnt stop it until ctrl-c is pressed in the terminal
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()