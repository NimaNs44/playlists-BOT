import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# دریافت توکن و آیدی کانال از متغیرهای محیطی
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

# بررسی و چاپ توکن و آی‌دی کانال برای اطمینان
if not TOKEN:
    raise ValueError("No TOKEN provided")
if not CHANNEL_ID:
    raise ValueError("No CHANNEL_ID provided")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('سلام! من یک بات هستم که به هر پستی کپشن اضافه می‌کنم و آن را به کانال ارسال می‌کنم.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    message = update.message
    new_caption = '@NimaPlaylists'

    if message.photo:
        photo = message.photo[-1].file_id
        await context.bot.send_photo(chat_id=CHANNEL_ID, photo=photo, caption=new_caption)
    elif message.video:
        video = message.video.file_id
        await context.bot.send_video(chat_id=CHANNEL_ID, video=video, caption=new_caption)
    elif message.audio:
        audio = message.audio.file_id
        await context.bot.send_audio(chat_id=CHANNEL_ID, audio=audio, caption=new_caption)
    else:
        await update.message.reply_text('فقط عکس، ویدئو و فایل‌های صوتی پشتیبانی می‌شود.')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO | filters.AUDIO, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
