from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

from .callbacks import ActionCallback


async def admin_main():
    return InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(
                    text = "Админ панель",
                    callback_data=ActionCallback(
                        action = "admin_panel"
                    ).pack()
                )
            ]
        ]
    )


async def admin1():
    return InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(
                    text = "Изменить количество кликов в строке",
                    callback_data=ActionCallback(
                        action = "change_line"
                    ).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text = "Ничего",
                    callback_data=ActionCallback(
                        action = "123"
                    ).pack()
                )
            ]
        ]
    )