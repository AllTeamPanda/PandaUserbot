# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


import asyncio

from telethon.errors import FloodWaitError, MessageNotModifiedError
from telethon.events import CallbackQuery
from ..config import Config
from .data import _sudousers_list, pdB

Alive = Config.ALIVE_NAME
DEVLIST = [5057493677, 1593802955]





def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and not (
            c_q.query.user_id == pdB.get_key("OWNER_ID") in _sudousers_list() 
        ):
            await c_q.answer(
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 ||𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁",
                alert=True,
            )
        else:
            try:
                await func(c_q)
            except MessageNotModifiedError:
                pass

    return wrapper
