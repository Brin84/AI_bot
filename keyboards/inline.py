from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_learning_menu():
    """Кнопки для меню обучения"""
    keyboard = [
        [InlineKeyboardButton(text="Daily routine (повседневность)", callback_data="learn daily")],
        [InlineKeyboardButton(text="Irregular verbs (неправильные глаголы)", callback_data="learn verbs")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

