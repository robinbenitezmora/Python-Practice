from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater('your_own_API_Token got from BotFather', use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello sir, Welcome to the Bot. Please write /help to see the commands.')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('This is a help message. Please write /start to start the bot.')

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text('https://mail.google.com/mail/u/0/#inbox')

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', help))

updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()
