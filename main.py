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

init_db()

sessions = {}

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
        await message.answer("Вход выполнен успешно!", reply_markup=main_menu)
        await state.clear()
    else:
        await message.answer("Неверный логин или пароль!")
    
@dp.message(Command("shop"))
async def shop(message: Message):
    if message.from_user.id not in sessions:
        return await message.answer("Вы не авторизованы! /login")
    await message.answer("Выберите дизайн:", reply_markup=designs)
    await state.set_state(Shop.design)

@dp.callback_query(Shop.design)
async def choose_design(callback: CallbackQuery, state: FSMContext):
    design = callback.data.split(":")[1]
    await state.update_data(design=design)
    await callback.message.edit_text("Вы выбрали дизайн: {design}\nВыберите цвет: ", reply_markup=colors)
    await state.set_state(Shop.color)
    
@dp.callback_query(Shop.color)
async def choose_color(callback: CallbackQuery, state: FSMContext):
    color = callback.data.split(":")[1]
    await state.update_data(color=color)
    await callback.message.edit_text("Вы выбрали цвет: {color}\nВыберите размер: ", reply_markup=sizes)
    await state.set_state(Shop.size)
    
@dp.callback_query(Shop.size)
async def choose_size(callback: CallbackQuery, state: FSMContext):
    size = callback.data.split(":")[1]
    await state.update_data(size=size)
    await callback.message.edit_text("Вы выбрали размер: {size}",reply_markup=confirm)
    await state.set_state(Shop.design)
    
@dp.callback_query(Shop.confirm)
async def confirm_order(callback: CallbackQuery, state: FSMContext):
    if callback.data == "confirm:yes":
        data = await state.get_data()
        add_cart(callback.from_user.id, "Кресло", data["color"], data["size"], data["design"], 1000)
        await callback.message.edit_text("Заказ добавлен в корзину!")
    else:
        await callback.message.edit_text("Заказ отменен!")
    await state.clear()
    
    

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


