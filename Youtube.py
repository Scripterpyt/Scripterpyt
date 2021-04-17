import os, requests
from colorama import Fore
import webbrowser

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

                                                {Fore.LIGHTGREEN_EX}Made by Scripter#5090
                                                {Fore.LIGHTBLUE_EX} Youtube: Scripter
                                                
    ''')
    print("")
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}1{Fore.LIGHTWHITE_EX}] {Fore.RED}Youtube{Fore.BLUE}Channel')
    print("")
    print("")

    answer = input("> ")

    if answer == "1":
        webbrowser.open_new_tab('https://www.youtube.com/channel/UCkkKkHBCUlRKN7RQVGyL3jw')

    else:
        print("")
        Youtube()


ResetTool()