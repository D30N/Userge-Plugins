# by Deonnn

import asyncio

from userge import userge


@userge.on_cmd("wahack$", about={'header': "WhatsApp prank by @Deonnn"})
async def brain_func(message):
    animation_chars = [

        

            "Looking for WhatsApp databases in targeted person...",

            " User online: `True`\nTelegram access: `True`\nRead Storage: `True`",

            "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",

            "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",

            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",    

            "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",

            "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",

            "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",

            "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",

            "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",

            "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",

            "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",

            "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",

            "Hacking complete!\n`Uploading file...`",

            "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"

        ]

    for i in range(15):
        await asyncio.sleep(2)
        await message.edit(animation_chars[i % 15])
