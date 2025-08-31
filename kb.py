from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="/shop"),
            KeyboardButton(text="/cart"),
            KeyboardButton(text="/logout")
        ]
    ],
    resize_keyboard=True
)

colors = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Белый", callback_data="color:white"),
        InlineKeyboardButton(text="Черный", callback_data="color:black"),
        InlineKeyboardButton(text="Дерево", callback_data="color:wood")
    ]
])


sizes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="S", callback_data="size:S"),
        InlineKeyboardButton(text="M", callback_data="size:M"),
        InlineKeyboardButton(text="L", callback_data="size:L")
    ]
])

designs = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Классика", callback_data="design:classic"),
        InlineKeyboardButton(text="Модерн", callback_data="design:modern"),
        InlineKeyboardButton(text="Лофт", callback_data="design:loft")
    ]
])

confirm = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Добавить в корзину", callback_data="confirm:yes"),
        InlineKeyboardButton(text="Отменить", callback_data="confirm:no")
    ]
])
