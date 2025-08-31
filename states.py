from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    name = State()
    password = State()

class Login(StatesGroup):
    name = State()
    password = State()
   

class Shop(StatesGroup):
    color = State()
    size = State()
    design = State()
    confirm = State()
    
    