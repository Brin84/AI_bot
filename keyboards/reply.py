from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def reply_start():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Давай начнем наш диалог')],
            ],
            resize_keyboard=True,
            one_time_keyboard=True
    )


