import os

import requests
import telegram
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telegram.Bot(token=TOKEN)


def send_photo_link(update: Update, context: CallbackContext):
    file_id = update.message.document.file_id
    file_url = bot.get_file(file_id).file_path
    photo_url = bot.get_file(file_id)['file_path']
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=photo_url)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Send me a photo to get a link to it.")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document.category("image"), send_photo_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
