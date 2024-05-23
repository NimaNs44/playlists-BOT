import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = os.getenv('6547251456:AAE0E6w7vqYWxqgqHG3V83RFloV1dKXg3pE')
CHANNEL_ID = os.getenv('NimaPlaylists')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من یک بات هستم که به هر پستی کپشن اضافه می‌کنم و آن را به کانال ارسال می‌کنم.')

def handle_message(update: Update, context: CallbackContext) -> None:
    message = update.message
    new_caption = '@NimaPlayLists'

    if message.photo:
        photo = message.photo[-1].file_id
        context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=new_caption)
    elif message.video:
        video = message.video.file_id
        context.bot.send_video(chat_id=CHANNEL_ID, video=video, caption=new_caption)
    elif message.audio:
        audio = message.audio.file_id
        context.bot.send_audio(chat_id=CHANNEL_ID, audio=audio, caption=new_caption)
    else:
        update.message.reply_text('فقط عکس و ویدئو پشتیبانی می‌شود.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video | Filters.audio, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
