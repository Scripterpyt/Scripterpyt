import os, webbrowser, requests
from colorama import Fore

def ResetTool():
    while 1:
        Youtube()
        os.system("pause")


def Youtube():
    os.system("cls && title Youtube-Multi-Tool")
    print(f'''
                            {Fore.RED} ▄▀▀▄ ▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀█{Fore.BLUE}▀▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄   ▄▀▀█▄▄▄▄ 
                            {Fore.RED}█   ▀▄ ▄▀ █      █ █   █    █ █    █{Fore.BLUE}  ▐ █   █    █ ▐ ▄▀   █ ▐  ▄▀   ▐ 
                            {Fore.RED}▐     █   █      █ ▐  █    █  ▐   █ {Fore.BLUE}    ▐  █    █    █▄▄▄▀    █▄▄▄▄▄  
                            {Fore.RED}      █   ▀▄    ▄▀   █    █      █  {Fore.BLUE}      █    █     █   █    █    ▌  
                            {Fore.RED}    ▄▀      ▀▀▀▀      ▀▄▄▄▄▀   ▄▀   {Fore.BLUE}       ▀▄▄▄▄▀   ▄▀▄▄▄▀   ▄▀▄▄▄▄   
                            {Fore.RED}    █                         █     {Fore.BLUE}               █    ▐    █    ▐   
                            {Fore.RED}    ▐                         ▐     {Fore.BLUE}               ▐         ▐        

                                                {Fore.LIGHTGREEN_EX}Made by Scripter#4908
                                                {Fore.LIGHTBLUE_EX} Youtube: Scripter
                                                
    ''')
    print("")
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] {Fore.RED}Youtube{Fore.BLUE}Channel')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}2{Fore.LIGHTWHITE_EX}] {Fore.RED}Nmap{Fore.BLUE}Scanner')
    print("")
    print("")

    a = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Yout\u001b[38;5;49mube\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

    if a == "1":
        webbrowser.open_new_tab('https://www.youtube.com/channel/UCkkKkHBCUlRKN7RQVGyL3jw')

    elif a == "2":
        print("Welcome to the Nmap Scanner!")
        api = 'https://api.hackertarget.com/nmap/?q='
        target = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

        attack = api + target

        req = requests.get(attack)

        nmaptext = req.text

        print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget \u001b[38;5;50mFound\u001b[38;5;51m]═>\u001b[38;5;7m " + str(nmaptext))


    else:
        Youtube()


ResetTool()