from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
import requests
import logging
import time
import os
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("Token_dog")

def start(update, context) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Jainam", url='https://t.me/jainamoswal'),
            InlineKeyboardButton("Channel", url='https://t.me/bot_updates_jainamoswal'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(f'Hey {update.effective_user.first_name},\nUse the following commands.\n______________________________________\n/dog - Sends you the random dog image.\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\nTill now, only one command will work. But you can join the group for more updates.', reply_markup=reply_markup)


def button(update, context) -> None:
    query = update.callback_query

    query.answer()

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

run_async
def dog(update, context):
    url = get_image_url()
    context.bot.send_photo(chat_id=update.message.chat_id, photo=url, caption='Made by <a href="https://t.me/jainamoswal">Jainam Oswal</a> with ❤️ from  <a href="https://www.google.com/search?sxsrf=ALeKk03RbM4P4prPlO-eFIZuHBXBnI-gbA%3A1604760768088&ei=wLSmX6fqBMGcmgf7sLvwDQ&q=INDIA&oq=INDIA&gs_lcp=CgZwc3ktYWIQAzIHCC4QJxCTAjIECC4QQzIKCAAQsQMQFBCHAjIQCC4QsQMQxwEQowIQFBCHAjIFCAAQsQMyAggAMgUIABCxAzIFCAAQsQMyBQgAELEDMgsILhCxAxDHARCjAjoKCC4QyQMQJxCTAjoECCMQJzoECAAQQzoICAAQsQMQgwE6CAguELEDEIMBOgoIABCxAxCDARBDUModWPclYMoyaABwAXgBgAHiAYgBmQaSAQUwLjIuMpgBAaABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwinyp_c1_DsAhVBjuYKHXvYDt4Q4dUDCA0&uact=5">INDIA.</a>', parse_mode='HTML')
    

def main():
    updater = Updater(TOKEN, use_context=True)
    PORT = int(os.environ.get('PORT', '8443'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',dog))
    dp.add_handler(CommandHandler('start',start))
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://short-dfgh.herokuapp.com/" + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
