from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio
import nest_asyncio

nest_asyncio.apply()

TOKEN = "7892363140:AAEdC_aZM03Gvc_Gp3Oj8zHJq_Rt1dXjCUw"

# ======= Обработчик кнопок =======
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.message.reply_text("Я простой Telegram-бот с меню 😊")
    elif query.data == "help":
        await query.message.reply_text("Пока я умею только показывать кнопки 😄")
    elif query.data == "contact":
        await query.message.reply_text("Связаться с разработчиком: @your_username")
    else:
        await query.message.reply_text("Неизвестная команда 😅")

# ======= Команда /start =======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("ℹ️ О боте", callback_data="about")],
        [InlineKeyboardButton("💬 Помощь", callback_data="help")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери действие:", reply_markup=reply_markup)

# ======= Главная функция =======
async def main():
    print("Бот запущен ✅")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    await app.run_polling()

# ======= Запуск =======
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())