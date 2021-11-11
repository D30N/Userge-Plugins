# Custom plugin by @Deonnn 
import os
import asyncio
import requests
from userge import userge, Message, pool

@userge.on_cmd("uptg", about={
    'header': "Update your app please!",
    'usage': "{tr}uptg"})
async def uptg_(message: Message):
    """uptg_"""
    query = message.input_or_reply_str
    if not query:
        await message.err("Command error")
        return
    query_encoded = query.replace(" ", "+")
    lmg_url = f"tg://need_update_for_some_feature/"
    await message.edit(f"Hmmm.../n[UPDATE YOUR APP]({lmg_url})")
