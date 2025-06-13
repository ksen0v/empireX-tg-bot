from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery
from typing import Union

from config_loader import ADMIN_ID


class AdminFilter(Filter):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(
        self,
        event: Union[Message, CallbackQuery],
        *args,
        **kwargs
    ) -> bool:
        return event.from_user.id == self.admin_ids


# Создаем инстанс фильтра
IsAdmin = AdminFilter(admin_ids=ADMIN_ID)