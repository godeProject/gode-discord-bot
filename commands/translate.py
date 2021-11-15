import requests
from commands.base_command import BaseCommand


class conv(BaseCommand):
    def __init__(self):
        description = "Convert argument given using g;ode API"
        params = ["input"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        url = "https://api.guntxjakka.me/api/v1/getans?phrase="
        actualparams = ' '.join(params)
        r = requests.get(url+actualparams)
        r.encoding = 'utf-8'
        ans = r.json()
        try:
            pmsg = ans['results']
            msg = 'Results: '+str(pmsg)
        except: 
            if ans['status']==400:
                msg = ans['Error']
            else:
                msg = ans
        await message.channel.send(msg)
