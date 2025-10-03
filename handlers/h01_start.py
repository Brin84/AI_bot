from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove

from keyboards.inline import get_learning_menu
from settings_ai.settings import ask

from keyboards.reply import reply_start
from states.creator import Creator
from data.topics import daily_routine_words, irregular_verbs

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    """обработка команды /start"""
    photo = FSInputFile("media/start_file.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Привет \nЯ готов дать ответ на любой вопрос.\nНажми кнопку ниже:",
        reply_markup=reply_start()
    )


@router.message(F.text == "Давай начнем наш диалог")
async def open_learning_menu(message: Message):
    await message.answer(
        "Выбери, что хочешь изучать 👇",
        reply_markup=get_learning_menu()
    )


@router.message(Creator.wait)
async def antiflood(message: Message):
    await message.answer("Ожидайте, Ваш запрос обрабатывается")


@router.message()
async def generate(message: Message, state: FSMContext):
    await state.set_state(Creator.wait)
    response = await ask(message.text)
    await message.answer(response)
    await state.clear()
