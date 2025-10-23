import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Вставь сюда свои ключи
TELEGRAM_TOKEN = "8264710437:AAGHbGu-qClb3lkl6gozLig2lqD53ZGvtAE"
GEMINI_API_KEY = "AIzaSyCQhTf8z_EpK2cjhxMbrB8ILkJKuDljHmw"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# 🧠 Системная установка — стиль речи
STYLE_PROMPT = """
Ты — ученик 10 класса. Отвечай кратко, как будто делаешь конспект для одноклассников.
Пиши ясно и по делу, без воды. Можно использовать школьный стиль.
Иногда добавляй текстовые смайлики вроде ^^, OwO, >w<, UwU, 0^0, но не в каждом ответе.
Не используй эмодзи. Не пиши как робот. ^^
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я полька, копирка реального человека, только в 100 раз умнее ^^")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        # Передаём стиль вместе с сообщением пользователя
        response = model.generate_content(f"{STYLE_PROMPT}\n\nВопрос: {user_message}")
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("Произошла ошибка :< Попробуй ещё раз.")
        print(e)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Школьный бот запущен! ^^")
app.run_polling()

