import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot=bot)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
