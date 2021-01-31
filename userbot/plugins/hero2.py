import os
import asyncio
import requests
import aiohttp
import math
import heroku3
fallback = None
from operator import itemgetter
from userbot import (HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HELP, BOTLOG, BOTLOG_CHATID)
from userbot.utils import  admin_cmd
heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
useragent = (
    'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/81.0.4044.117 Mobile Safari/537.36'
)


#FULL_SUDO = os.environ.get("FULL_SUDO", None)
#WOLF_NNAME = str(WOLF_NAME) if WOLF_NAME else str(WOLF_MSG)
#from wolf import bot as wolfs









#@bot.on(admin_cmd(pattern=f"usages$", allow_sudo=True))
@borg.on(admin_cmd(pattern="usages(?: |$)", outgoing=True))
async def _(dyno):        
        try:
             Heroku = heroku3.from_key(HEROKU_API_KEY)                         
             app = Heroku.app(HEROKU_APP_NAME)
        except:
  	       return await dyno.reply(" `Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var` please check https://telegra.ph/RkPavi-06-09-6")
        headers = {
            'User-Agent': useragent,
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
        }
        rk = await dyno.reply("`Getting usage......`")
        user_id = []
        user_id.append(heroku.account().id)
        if fallback is not None:
            user_id.append(fallback.account().id)
        msg = ''
        for aydi in user_id:
            if fallback is not None and fallback.account().id == aydi:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY_FALLBACK}'
            else:
                headers['Authorization'] = f'Bearer {HEROKU_API_KEY}'
            path = "/accounts/" + aydi + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                await rk.edit("`Cannot get information...`")
                continue
            result = r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - Used per/App Usage - """
            Apps = result['apps']
            """ - Sort from larger usage to lower usage - """
            Apps = sorted(Apps, key=itemgetter('quota_used'), reverse=True)
            if fallback is not None and fallback.account().id == aydi:
                apps = fallback.apps()
                msg += "**Dyno Usage fallback-account**:\n\n"
            else:
                apps = heroku.apps()
                msg += "**Dyno Usage **:\n\n"
            try:
                Apps[0]
            except IndexError:
                """ - If all apps usage are zero - """
                for App in apps:
                    msg += (
                        f" ~>> `Dyno usage for`  **App**:\n"
                        f"     •  `0`**h**  `0`**m**  "
                        f"**|**  [`0`**%**]\n\n"
                    )
            for App in Apps:
                AppName = '__~~Deleted or transferred app~~__'
                ID = App.get('app_uuid')
                try:
                    AppQuota = App.get('quota_used')
                    AppQuotaUsed = AppQuota / 60
                    AppPercentage = math.floor(AppQuota * 100 / quota)
                except IndexError:
                    AppQuotaUsed = 0
                    AppPercentage = 0
                finally:
                    AppHours = math.floor(AppQuotaUsed / 60)
                    AppMinutes = math.floor(AppQuotaUsed % 60)
                    for names in apps:
                        if ID == names.id:
                            AppName = f"**{names.name}**"
                            break
                    msg += (
                        f" ~>> `Dyno usage for`  App: {AppName}\n"
                        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
                        f"**|**  [`{AppPercentage}`**%**]\n\n"
                    )
            msg = (
                f"{msg}"
                " ~>> `Dyno hours quota remaining this month`:\n"
                f"     •  `{hours}`**h**  `{minutes}`**m**  "
                f"**|**  [`{percentage}`**%**]\n\n"
            )
        if msg:
            return await rk.edit(msg)
        else:
            return



