from aiogram.filters import BaseFilter
from aiogram.types import Message


list_admin=[5065503282]


class CheckAdmin(BaseFilter):
    async def __call__(self, message: Message):
        if message.from_user.id in list_admin:
            return True