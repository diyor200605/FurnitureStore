from aiogram import Bot, Dispatcher, Router
import asyncio
from aiogram.types import  Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext


from database import init_db, add_user, get_user
from states import Register, Login, Shop
from kb import main_menu, colors, sizes, designs, confirm


token = "8269993752:AAGkdNjJmpZOJaefXhIugWwpIXhiCCzOHqE"

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать в магазин мебели!\n\nВыберите действие:\n\nРегистрация: /register\nВход: /login\nМагазин: /shop", reply_markup=main_menu)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


