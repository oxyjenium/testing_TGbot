from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from .filters import CheckAdmin

from . import keyboards

from .callbacks import ActionCallback

from .states import WaitMessage

from app.models import Stat


router = Router(name="admin")


@router.message(CheckAdmin(), F.text == '/admin')
async def proverka(message: Message):
    await message.answer(
        text='Вы админ',
        parse_mode="HTML",
        reply_markup=await keyboards.admin_main()
)


@router.callback_query(CheckAdmin(), ActionCallback.filter(F.action == 'admin_panel'))
async def proverka1(call: CallbackQuery):
    await call.message.answer(
        text = 'Вы в админ панеле',
        parse_mode="HTML",
        reply_markup= await keyboards.admin1()
    )


@router.callback_query(CheckAdmin(), ActionCallback.filter(F.action == 'change_line'))
async def proverka1(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        text = 'Введите номер строки, в который Вы хотите поменять количество кликов',
        parse_mode="HTML"
    )
    await state.set_state(WaitMessage.message1)


@router.message(CheckAdmin(), WaitMessage.message1)
async def proverka2(message: Message, state: FSMContext):
    await state.update_data(message1 = message.text)
    await message.answer(
        text = "Введите количество кликов",
        parse_mode="HTML"
    )
    await state.set_state(WaitMessage.message2)


@router.message(CheckAdmin(), WaitMessage.message2)
async def proverka2(message: Message, state: FSMContext):
    await state.update_data(message2 = message.text)
    states = await state.get_data()
    id = states.get('message1')
    kol = states.get('message2')
    print(id,kol)
    await Stat.filter(id=id).update(stats=kol)
    await message.answer(
        text="Информаци обновлена",
        parse_mode="HTML"
    )
    
    
    