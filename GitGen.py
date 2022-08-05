webhook = "" # paste your webhook between the ""
length = 3 # change this for a different length

#===================================================================================

import os
import sys
import random
import requests
import subprocess

from pystyle import *
from time import sleep

os.system("cls | mode 70,30")

banner = f'''
{" ██████╗ ██╗████████╗ ██████╗ ███████╗███╗   ██╗".center(70)}
{"██╔════╝ ██║╚══██╔══╝██╔════╝ ██╔════╝████╗  ██║".center(70)}
{"██║  ███╗██║   ██║   ██║  ███╗█████╗  ██╔██╗ ██║".center(70)}
{"██║   ██║██║   ██║   ██║   ██║██╔══╝  ██║╚██╗██║".center(70)}
{"╚██████╔╝██║   ██║   ╚██████╔╝███████╗██║ ╚████║".center(70)}
{" ╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝".center(70)}
'''
                                                

print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))
print("═"*70)

def restart():
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

os.system("title GitGen │ github.com/quentn69")

def internet_check():
    try:
        requests.get("https://www.google.com")
    except:
        print("You aren't connected to the internet.".center(70))
        print("Check your connection and try again.".center(70))
        print("═"*70)
        input()
        restart()

letters = "abcdefghijklmnopqrstuvwxyz1234567890"

with open('users.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()

def generate():
    with open("users.txt", "w+") as f:
        for i in range(20):
            user = ""
            for i in range(length):
                user = user + random.choice(letters)
            user = str(user)
            f.write(f"{user}\n")


def check():
    copped = []
    session = requests.Session()
    for username in usernames:
        c = session.get(f'https://github.com/{username}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 'Connection': 'keep-alive', }, timeout=60)
        status = c.status_code
        if status == 404:
            with open("hits.txt", "a") as f:
                f.write(f"{username}\n")
            copped.append(username)
            print(Colors.green + username.center(70))

        elif status == 200 or 204:
            print(Colors.red + username.center(70))
        
        else:
            print(Colors.yellow_to_red + "══════════════════════════════════════════════════════════════════════".center(70))
            print(Colors.yellow_to_red + f"Other Status Code = {status}".center(70))
            print(Colors.yellow_to_red + "══════════════════════════════════════════════════════════════════════".center(70))

    copped = '\n'.join(copped)
    data = {
    "content": f"**GitHub**\n🚨{len(username)}L Usernames🚨\n```{copped}```",
    "username": "github.com/quentn69",
    "avatar_url": "https://avatars.githubusercontent.com/u/107768845?v=4"}
    if len(copped) == 0:
        sleep(60)
        restart()
    else:
        try:
            requests.post(webhook, json=data)
        except:
            pass
        sleep(60)
        restart()


if __name__ == '__main__':
    generate()
    internet_check()
    check()
