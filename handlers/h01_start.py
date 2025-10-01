from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from settings_ai.settings import ask

from keyboards.reply import reply_start
from states.creator import Creator

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    """Реакция на команду /start"""
    photo = FSInputFile("media/start_file.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Привет, я помогу тебе изучить английский язык",
        reply_markup=reply_start()
        )

@router.message(F.text == "Я готов ответить на твой вопрос󠁧")
async def chat_start(message: Message):
    """Обработчик кнопки при старте"""
    await message.answer("",
                         reply_markup=ReplyKeyboardRemove())

@router.message(Creator.wait)
async def antiflood(message: Message):
    await message.answer("Ожидайте, Ваш запрос обрабатывается")


@router.message()
async def generate(message: Message, state: FSMContext):
    await state.set_state(Creator.wait)
    response = await ask(message.text)
    await message.answer(response)
    await state.clear()