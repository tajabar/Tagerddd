import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask

app = Flask(__name__)

# استبدل 'YOUR_BOT_TOKEN' بالتوكن الحقيقي
TOKEN = os.getenv("BOT_TOKEN")

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أنا بوت بايثون يعمل على Glitch 🐍🚀")

# رد على أي رسالة نصية
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"لقد أرسلت: {text}")

# تشغيل البوت
def run_bot():
    application = Application.builder().token(TOKEN).build()

    # إضافة Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # بدء البوت
    application.run_polling()

# تشغيل خادم ويب لمنع Glitch من الإيقاف
@app.route('/')
def home():
    return "البوت يعمل!"

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=3000)
