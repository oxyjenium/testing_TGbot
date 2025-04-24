from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from .states import Information

from . import keyboards
from .callbacks import ActionCallback

from app.models import Stat

router = Router(name="kliker")


@router.message(F.text == 'Начать кликать')
async def start_klik(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(
        text='Вы перешли в режим кликера',
        parse_mode="HTML",
        reply_markup=await keyboards.base()
    )
    await state.update_data(klik=0)
    


@router.callback_query(
    ActionCallback.filter(F.action == "plus_klik")
)
async def klik_plus(call: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    klik = states.get('klik')
    await state.update_data(klik=klik+1)
    states = await state.get_data()
    kol = states.get('klik')
    await call.message.edit_text(
        text = f'Сейчас у вас {kol} кликов',
        parse_mode="HTML",
        reply_markup=await keyboards.base()
    )

@router.callback_query(
    ActionCallback.filter(F.action == "minus_klik")
)
async def klik_minus(call: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    klik = states.get('klik')
    await state.update_data(klik = klik-1)
    states = await state.get_data()
    kol = states.get('klik')
    await call.message.edit_text(
        text = f'Сейчас у вас {kol} кликов',
        parse_mode="HTML",
        reply_markup=await keyboards.base()
    )
    

@router.message(Command('reg'))
async def registration(message: Message, state: FSMContext):
    await message.answer('Вы перешли в режим регистрации своего результата. Напишите свое имя')
    states = await state.get_data()
    kol = states.get('klik')
    await state.update_data(stats=kol)
    await state.set_state(Information.name)

@router.message(Information.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer('Введите ваш возраст')
    await state.set_state(Information.age)

@router.message(Information.age)
async def reg_age(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    states = await state.get_data()
    await message.answer(
        text=f"Вы ввели следующую информацию.\nИмя: {states.get('name')}\nВозраст: {states.get('age')}\nКоличество кликов: {states.get('stats')}",
        reply_markup=await keyboards.reg_stats()
)
    
    
@router.callback_query(
    ActionCallback.filter(F.action == 'stats_reg')
)
async def register1(call: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    kol = states.get('klik')
    await Stat.create(
        ident=call.message.from_user.id,
        stats=kol
    )
    await call.message.answer(
        text='Статистика внесена в базу данных',
        parse_mode="HTML",
        reply_markup=await keyboards.get_stats()
    )


@router.callback_query(
    ActionCallback.filter(F.action == 'stats_no_reg')
)
async def register2(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer(
        text='Статистика удалена',
        parse_mode="HTML"
    )


@router.callback_query(
    ActionCallback.filter(F.action == 'stats_get')
)
async def register2(call: CallbackQuery):
    info = await Stat.all()
    for spisok in info:
        await call.message.answer(
            text=f"id: {spisok.ident}\n Количество: {spisok.stats}"
        )