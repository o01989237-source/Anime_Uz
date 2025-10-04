from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("TOKEN")  # Railwaydagi environment variable
ADMIN_ID = int(os.getenv("ADMIN_ID", "7402408857"))

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom! Men 24/7 ishlaydigan anime botman 😊")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)