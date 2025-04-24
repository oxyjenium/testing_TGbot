from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
import os
import asyncio


from main.router import router as r1
from kliker.router import router as r2

from app.models import start_db

dp = Dispatcher()

async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))
    await start_db()
    dp.include_routers(r1,r2)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())