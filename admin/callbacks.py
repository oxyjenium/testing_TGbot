from aiogram.filters.callback_data import CallbackData


class ActionCallback(CallbackData, prefix="ac"):
	action: str
	object_id: int|str|None = None

