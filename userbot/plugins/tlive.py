# For @TeleBotHelp
"""Check if your userbot is working."""
import time
from datetime import datetime
from io import BytesIO
import os

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
#from userbot.__init__ import StartTime
#from var import  Var
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, sudo_cmd
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# ======CONSTANTS=========#
CUSTOM_ALIVE =  "Hey! I'm alive. All systems online and functioning normally!"
ALV_PIC = Config.ALIVE_PHOTTO
telemoji = "**✵**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@TeleBotSupport"


@bot.on(admin_cmd(outgoing=True, pattern="tlive"))
@bot.on(sudo_cmd(outgoing=True, pattern="tlive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    #uptime = get_readable_time((time.time() - StartTime))
    uptime = get_readable_time((time.time() - Lastupdate))
    if ALV_PIC:
        tele = f"**Welcome To TeleBot **\n\n"
        tele += f"`{CUSTOM_ALIVE}`\n\n"
        tele += (
            f"{telemoji} **Telethon version**: `1.19.0`\n{telemoji} **Python**: `3.8.3`\n"
        )
        tele += f"{telemoji} **TeleBot Version**: `2.0`\n"
        tele += f"{telemoji} **More Info**: @rootedcyberchannel\n"
        tele += f"{telemoji} **Sudo** : `disable`\n"
        tele += f"{telemoji} **TeleBot Uptime**: `{uptime}`\n"
        tele += f"{telemoji} **Database Status**: `All OK 👌!`\n"
        tele += (
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n"
        )
        tele += f"{telemoji} **Github :** [rooted-cyber](https://github.com/rooted-cyber/)\n"
        tele += f"{telemoji} **Channel :** [Channel](https://t.me/rootedcyberchannel)\n"
        tele += f"{telemoji} **Group :** [Group](https://t.me/rootedcyber1)\n\n"
        tele += f"{telemoji} **Check stats by** `.status` {telemoji}\n"
        tele += f"{telemoji} **Check plugin info** `.in <plugin name> or .plinfo <plugin name>` {telemoji}\n\n"
        tele += "    [✨ GitHub Repository ✨](https://github.com/rooted-cyber/My_Userbot)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/0670190de8e3bddea6d95.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To TeleBot **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{telemoji} **Telethon version**: `1.19.0` \n**Python**: `3.8.3`\n"
            f"{telemoji} **TeleBot Version**: `1.)`\n"
            f"{telemoji} **More Info**: @rootedcyberchannel\n"
            f"{telemoji} **Sudo** : `Disable`\n"
            f"{telemoji} **TeleBot Uptime**: `{uptime}`\n"
            f"{telemoji} **Database Status**: `All OK 👌!`\n"
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n"
            f"{telemoji} **Github :** [rooted-cyber](https://github.com/rooted-cyber/)\n"
            f"{telemoji} **Channel :** [Channel](https://t.me/rootedcyberchannel)\n"
            f"{telemoji} **Group :** [Group](https://t.me/rootedcyber1)\n\n"
            f"{telemoji} **Check stats by** `.status` {telemoji}\n"
            f"{telemoji} **Check plugin info** `.in <plugin name> or .plinfo <plugin name>` {telemoji}\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/rooted-cyber/My_Userbot)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
