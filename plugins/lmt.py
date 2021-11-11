# Custom plugin by @Deonnn 
import os
import asyncio
import requests
from userge import userge, Message, pool

@userge.on_cmd("lmt", about={
    'header': "Let me Search that for you real quick !!",
    'usage': "{tr}lmt [query | reply to msg]"})
async def lmg_(message: Message):
    """lmg_"""
    query = message.input_or_reply_str
    if not query:
        await message.err("Give something to LMT!")
        return
    query_encoded = query.replace(" ", "+")
    lmg_url = f"tg://search?query={query_encoded}"
    await message.edit(f"**Okey, let me Search that for you...**\n👉 Click here: [{query}]({lmg_url})\n`Thank me later 😉`")
