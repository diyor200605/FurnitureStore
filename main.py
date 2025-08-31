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
    await message.answer("Добро пожаловать в магазин мебели!\n\nВыберите действие:\n\nРегистрация: /register\nВход: /login\nМагазин: /shop")

@dp.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(Register.name)

@dp.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш пароль:")
    await state.set_state(Register.password)

@dp.message(Register.password)
async def register_password(message: Message, state: FSMContext):
    data = await state.get_data()
    add_user(message.from_user.id, data["name"], message.text)
    await message.answer("Регистрация прошла успешно!")
    await state.clear()

@dp.message(Command("login"))
async def login(message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(Login.name)

@dp.message(Login.name)
async def login_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш пароль:")
    await state.set_state(Login.password)

@dp.message(Login.password)
async def login_password(message: Message, state: FSMContext):
    data = await state.get_data()
    user = get_user(message.from_user.id)
    if user and user[2] == data["name"] and user[3] == message.text:
        await message.answer("Вход выполнен успешно!")
        await state.clear()
    else:
        await message.answer("Неверный логин или пароль!")
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


