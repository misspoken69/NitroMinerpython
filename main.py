# Configuration
import random, string, requests, colorama, webbrowser, keep_alive, flask
from colorama import Fore, Back, Style
import time

# Keep Alive 
keep_alive.keep_alive()

# Colorama
colorama.init()
time.sleep(2)

# Files
f1 = open('HitsClassic.txt', 'a+')
f1.close()
f2 = open('HitsBoost.txt', 'a+')
f2.close()
f = open('License.txt', 'w', encoding='UTF-8')
f.write('''
███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       █████▒▄▄▄       ██▀███   ███▄ ▄███▓▓█████  ██▀███  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓██   ▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒████ ░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█▒  ░░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒█░    ▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ▒ ░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░     ░       ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒      ░ ░     ░   ▒     ░░   ░ ░      ░      ░     ░░   ░ 
         ░  ░              ░         ░ ░                  ░  ░   ░            ░      ░  ░   ░     

Nitro Farmer modified by "Misspoken.\n
Warning\nThis tool is against Discord ToS, by using this tool your account could be banned. 
I don't take responsibility for your actions.

https://www.youtube.com/channel/UCmBZT8jrvTKZfEH52AVDpAw - My YouTube Channel
https://discord.gg/TyScsfHpQt - My Discord Server
''')

f.close()

# Title
print(Fore.WHITE + """
 ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       █████▒▄▄▄       ██▀███   ███▄ ▄███▓▓█████  ██▀███  
 ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒   ▓██   ▒▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒████ ░▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█▒  ░░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒█░    ▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ▒ ░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░     ░       ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒      ░ ░     ░   ▒     ░░   ░ ░      ░      ░     ░░   ░ 
         ░  ░              ░         ░ ░                  ░  ░   ░            ░      ░  ░   ░     
""" + Style.RESET_ALL)

print(Fore.WHITE + '[' + Fore.CYAN + '!' + Fore.WHITE + ']' + Fore.GREEN + ' Starting Nitro Famer')
time.sleep(2)

# Values
nitro = input(f'{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] {Fore.RED}Select Nitro: {Fore.WHITE}(Boost or Classic){Fore.RED}:{Fore.YELLOW} ')

# Generator
print(Style.RESET_ALL)
if "Boost" in nitro:
  while True:
    codeboost = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    r = requests.get(f'https://discordapp.com/api/v8/entitlements/gift-codes/{codeboost}?with_application=false&with_subscription_plan=true')
    if r.status_code == 200:
      print(Fore.GREEN + f'[+] Valid Nitro Code >' + Style.RESET_ALL + f' https://discord.gift/{codeboost}')
      f2 = open('HitsBoost.txt', 'a+')
      f2.write(f'[+] Valid Boost Code > https://discord.gift/{codeboost}\n')
      f2.close()
    else:
      print(Fore.RED + '[-] Invalid >' + Style.RESET_ALL + f' https://discord.gift/{codeboost}')

print(Style.RESET_ALL)
if "Classic" in nitro:
  while True:
    codeclassic = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    r = requests.get(f'https://discordapp.com/api/v8/entitlements/gift-codes/{codeclassic}?with_application=false&with_subscription_plan=true')
    if r.status_code == 200:
      print(Fore.GREEN + f'[+] Valid >' + Style.RESET_ALL + f' https://discord.gift/{codeclassic}')
      f1 = open('HitsClassic.txt', 'a+')
      f1.write(f'[+] Valid > https://discord.gift/{codeclassic}\n')
      f1.close()
    else:
      print(Fore.RED + '[-] Invalid >' + Style.RESET_ALL + f' https://discord.gift/{codeclassic}')
