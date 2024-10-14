from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_base = [
    [KeyboardButton(text='Отправиться в путешествие')],
    [KeyboardButton(text='Помощь')]
]

base_keyboard = ReplyKeyboardMarkup(
        keyboard=kb_base,
        resize_keyboard=True,
        input_field_placeholder = 'Время отправиться в путешествие'
    )