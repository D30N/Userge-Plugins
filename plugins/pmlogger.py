import os
from userge import userge, Message
from pyrogram import filters
from pyrogram.errors import FloodWait

PM_LOG = int(os.environ.get("PM_LOG", "-1001457141157"))


@userge.on_message(filters.private & filters.incoming & ~filters.bot)
async def hlo(b, m):
    try: 
        await m.forward(
            chat_id=PM_LOG,
            disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        print(e)
        pass
