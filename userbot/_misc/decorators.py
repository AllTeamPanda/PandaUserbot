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




def get_all_pros() -> list:
    """Get All Users , Sudo + Owners + Other Clients"""
    users = list(Config.SUDO_USERS)
    if pdB.get_key("OWNER_ID"):
        users.append(pdB.get_key("OWNER_ID"))
    return users


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        users = get_all_pros()
        if c_q.query.user_id == users:
            try:
                await func(c_q)
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModifiedError:
                pass
        else:
            await c_q.answer(
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 || 𝐎𝐰𝐧𝐞𝐫: {Alive}\n\n𝗖𝗿𝗲𝗮𝘁𝗲 𝗯𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗣𝗮𝗻𝗱𝗮𝗨𝘀𝗲𝗿𝗯𝗼𝘁",
                alert=True,
            )

    return wrapper
