import requests
import urllib
import json
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
        msg = r.json()
        await message.channel.send(msg)
