# Custom plugin by @Deonnn 
import os
import asyncio
import requests
from userge import userge, Message, pool

@userge.on_cmd("lmy", about={
    'header': "Let me YouTube that for you real quick !!",
    'usage': "{tr}lmg [query | reply to msg]"})
async def lmg_(message: Message):
    """lmy_"""
    query = message.input_or_reply_str
    if not query:
        await message.err("Give something to LMY!")
        return
    query_encoded = query.replace(" ", "+")
    lmg_url = f"https://www.youtube.com/results?search_query={query_encoded}"
    await message.edit(f"**Okey, let me YouTube that for you...**\n👉 Click here: [{query}]({lmg_url})\n`Thank me later 😉`")
