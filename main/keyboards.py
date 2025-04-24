from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


async def main():
    return ReplyKeyboardMarkup(
        keyboard=[
        [
            KeyboardButton(
                text = 'Начать кликать'
            )
        ],   
        [
            KeyboardButton(
                text = 'Для чего этот бот?'
            )
        ]
    ]
)