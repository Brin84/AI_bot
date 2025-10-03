from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove, CallbackQuery

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


@router.callback_query(F.data == "learn daily")
async def learn_daily_routine_words(callback: CallbackQuery):
    await callback.message.answer(daily_routine_words, parse_mode="Markdown")
    await callback.answer()


@router.callback_query(F.data == "learn verbs")
async def learn_verbs(callback: CallbackQuery):
    await callback.message.answer(irregular_verbs, parse_mode="Markdown")
    await callback.answer()


@router.message(Creator.wait)
async def antiflood(message: Message):
    await message.answer("Ожидайте, Ваш запрос обрабатывается")


@router.message()
async def generate(message: Message, state: FSMContext):
    await state.set_state(Creator.wait)
    response = await ask(message.text)
    await message.answer(response)
    await state.clear()
