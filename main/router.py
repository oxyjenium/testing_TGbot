from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from .service import text1

from . import keyboards

from app.models import User


router = Router(name='main')


@router.message(CommandStart())
async def command_start(message: Message):
    tg_id = message.from_user.id
    username = message.from_user.first_name
    user_list = await User.all().values('id')
    ids = [item['id'] for item in user_list] 
    if tg_id not in ids:
        await User.create(id=tg_id, username=username)
    await message.answer(
        text='Привет, уважаемый пользователь!',
        parse_mode='HTML',
        reply_markup=await keyboards.main()
    )


@router.message(F.text == 'Для чего этот бот?')
async def info_bot(message: Message):
    await message.delete()
    await message.answer(
        text=f"{text1()}",
        parse_mode='HTML'
)