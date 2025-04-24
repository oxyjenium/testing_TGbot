from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

from .callbacks import ActionCallback


async def base():
    return InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(
                    text = 'Плюс клик',
                    callback_data = ActionCallback(
                        action = "plus_klik"
                    ).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text = 'Минус клик',
                    callback_data = ActionCallback(
                        action = "minus_klik"
                    ).pack()
                )
            ]
        ]
    )
    

async def reg_stats():
    return InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(
                    text = 'Занести результат в базу данных',
                    callback_data=ActionCallback(
                        action='stats_reg'
                    ).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text = 'Не заносить результат в базу данных',
                    callback_data=ActionCallback(
                        action='stats_no_reg'
                    ).pack()
                )
            ]
        ]
    )


async def get_stats():
    return InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(
                    text = 'Вывести базу данных',
                    callback_data=ActionCallback(
                        action='stats_get'
                    ).pack()
                )
            ]
        ]
    )