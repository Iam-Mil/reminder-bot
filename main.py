import asyncio
import logging
from aiogram import Dispatcher, Router, types, Bot, utils
from aiogram.filters import CommandStart, Command
from const import api_key


router = Router()
dp = Dispatcher()
bot = Bot(token=api_key)


async def main():
    logger = logging.getLogger('aiogram')
    logger.setLevel(logging.INFO)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
