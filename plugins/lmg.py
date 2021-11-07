# Custom plugin by @Deonnn 
import os
import asyncio
import requests
from userge import userge, Message, pool

@userge.on_cmd("lmg", about={
    'header': "Let me Google that for you real quick !!",
    'usage': "{tr}lmg [query | reply to msg]"})
async def lmg_(message: Message):
    """lmg_"""
    query = message.input_or_reply_str
    if not query:
        await message.err("Give something to LMG!")
        return
    query_encoded = query.replace(" ", "+")
    lmg_url = f"http://google.com/search?q={query_encoded}"
    await message.edit(f"**Okey, let me Google that for you...**\n👉 Click here: [{query}]({lmg_url})\n`Thank me later 😉`")
