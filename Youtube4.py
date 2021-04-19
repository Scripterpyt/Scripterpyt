import os, webbrowser, requests
from colorama import Fore
from urllib.request import urlopen
from tkinter import Tk
from tkinter.filedialog import askopenfilename

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
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}3{Fore.LIGHTWHITE_EX}] {Fore.RED}Site-Links{Fore.BLUE}Grabber')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}4{Fore.LIGHTWHITE_EX}] {Fore.RED}HTTP{Fore.BLUE}Header')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}5{Fore.LIGHTWHITE_EX}] {Fore.RED}CTF-User{Fore.BLUE}Hunter')
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTCYAN_EX}6{Fore.LIGHTWHITE_EX}] {Fore.RED}Proxy{Fore.BLUE}Checker')
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

    elif a == "3":
        print("Welcome to my Site-Link Grabbing Script")
        api = 'https://api.hackertarget.com/pagelinks/?q='
        target = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

        attack = api + target

        req = requests.get(attack)

        gettext = req.text

        splitlinessssss = gettext.splitlines()

        for x in splitlinessssss:
            print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget \u001b[38;5;50mFound\u001b[38;5;51m]═>\u001b[38;5;7m " + str(x))

    elif a == "4":
        print("Welcome to my HTTP Header Script!")
        api = 'https://api.hackertarget.com/httpheaders/?q='
        target = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

        attack = api + target

        req = requests.get(attack)

        gettext = req.text

        splitlinessss = gettext.splitlines()

        for x in splitlinessss:
            print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget \u001b[38;5;50mFound\u001b[38;5;51m]═>\u001b[38;5;7m " + str(x))
    
    elif a == "5":
        print("Welcome to the CTF-User Hunter!")
        URLS = [
            'https://instagram.com/',
            'https://twitter.com/',
            'https://www.facebook.com/',
            'https://www.youtube.com/',
            'https://www.reddit.com/user/',
            'https://www.pinterest.com/',
            'https://www.github.com/',
            'https://www.flickr.com/people/',
            'https://steamcommunity.com/id/',
            'https://soundcloud.com/',
            'https://disqus.com/',
            'https://about.me/',
            'https://imgur.com/user/',
            'https://flipboard.com/@',
            'https://slideshare.net/',
            'https://rive.app/a/',
            'http://forum.3dnews.ru/member.php?username=',
            'https://500px.com/',
            'https://www.7cups.com/@',
            'https://www.9gag.com/u/',
            'https://about.me/',
            'https://independent.academia.edu/',
            'https://www.alik.cz/u/',
            'https://www.alltrails.com/members/',
            'https://archive.org/details/@',
            'https://asciinema.org/~',
            'https://ask.fedoraproject.org/u/',
            'https://ask.fm/',
            'https://audiojungle.net/user/',
            'https://blip.fm/',
            'https://badoo.com/profile/',
            'https://www.bandcamp.com/',
            'https://www.behance.net/',
            'https://bitcoinforum.com/profile/',
            'https://bodyspace.bodybuilding.com/',
            'https://buymeacoff.ee/',
            'https://buzzfeed.com/',
            'https://career.habr.com/',
            'https://cash.me/$',
            'https://beta.cent.co/@',
            'https://www.championat.com/user/',
            'https://www.chess.com/ru/member/',
            'https://www.cloob.com/name/',
            'https://community.cloudflare.com/u/',
            'https://www.clozemaster.com/players/',
            'https://www.codecademy.com/profiles/',
            'https://www.codechef.com/users/',
            'https://www.codewars.com/users/',
            'https://www.coroflot.com/',
            'https://www.countable.us/',
            'https://cracked.to/',
            'https://www.crunchyroll.com/user/',
            'https://dev.to/',
            'https://www.dailymotion.com/',
            'https://www.discogs.com/user/',
            'https://discuss.elastic.co/u/',
            'https://disqus.com/',
            'https://www.duolingo.com/profile/',
            'https://www.ebay.com/usr/',
            'https://ello.co/',
            'https://www.etsy.com/shop/',
            'https://euw.op.gg/summoner/userName=',
            'https://www.eyeem.com/u/',
            'https://facenama.com/',
            'https://www.fandom.com/u/',
            'https://www.filmo.gs/users/',
            'https://www.fiverr.com/',
            'https://www.flickr.com/people/',
            'https://fortnitetracker.com/profile/all/',
            'https://freelance.habr.com/freelancers/',
            'https://gdprofiles.com/',
            'https://www.getmyuni.com/user/',
            'https://giphy.com/',
            'https://www.github.com/',
            'https://gitlab.com/',
            'https://gitee.com/',
            'https://www.goodreads.com/',
            'http://en.gravatar.com/',
            'https://www.gumroad.com/',
            'https://forums.gunsandammo.com/profile/',
            'https://hackaday.io/',
            'https://forum.hackthebox.eu/profile/',
            'https://news.ycombinator.com/user?id=',
            'https://hackerone.com/',
            'https://hackerrank.com/',
            'https://houzz.com/user/',
            'https://hubpages.com/@',
            'https://hubski.com/user/',
            'https://www.ifttt.com/p/',
            'https://imageshack.us/user/',
            'https://imgup.cz/',
            'https://www.instructables.com/member/',
            'https://issuu.com/',
            'https://www.kaggle.com/',
            'https://www.kaggle.com/',
            'https://keybase.io/',
            'https://ws2.kik.com/user/',
            'https://launchpad.net/~',
            'https://leetcode.com/',
            'https://letterboxd.com/',
            'https://lichess.org/@/',
            'https://www.liveleak.com/c/',
            'https://lolchess.gg/profile/na/',
            'https://medium.com/@',
            'https://www.meetme.com/',
            'https://myanimelist.net/profile/',
            'https://myspace.com/',
            'https://www.native-instruments.com/forum/members?username=',
            'https://www.npmjs.com/~',
            'https://www.npmjs.com/package/',
            'https://namemc.com/profile/',
            'https://nationstates.net/nation=',
            'https://nationstates.net/region=',
            'https://notabug.org/',
            'https://opencollective.com/',
            'https://www.openstreetmap.org/user/',
            'https://opensource.com/users/',
            'https://community.oracle.com/people/',
            'https://otzovik.com/profile/',
            'https://ourdjtalk.com/members?username=',
            'https://forums.pcgamer.com/members/?username=',
            'https://pcpartpicker.com/user/',
            'https://psnprofiles.com/?psnId=',
            'https://pastebin.com/u/',
            'https://www.patreon.com/',
            'https://www.paypal.com/paypalme/',
            'https://play.google.com/store/apps/developer?id=',
            'https://plug.dj/@/',
            'https://pokemonshowdown.com/users/',
            'https://polarsteps.com/',
            'https://www.polygon.com/users/',
            'https://www.producthunt.com/@',
            'http://promodj.com/',
            'https://www.quora.com/profile/',
            'https://rateyourmusic.com/~',
            'https://www.realmeye.com/player/',
            'https://www.redbubble.com/people/',
            'https://www.reddit.com/user/',
            'https://repl.it/@',
            'https://www.reverbnation.com/',
            'https://www.roblox.com/user.aspx?username=',
            'https://rubygems.org/profiles/',
            'https://www.sbazar.cz/',
            'https://scratch.mit.edu/users/',
            'https://www.scribd.com/',
            'https://segmentfault.com/u/',
            'https://www.shitpostbot.com/user/',
            'https://community.signalusers.org/u/',
            'https://slideshare.net/',
            'https://www.smashcast.tv/api/media/live/',
            'https://www.smule.com/',
            'https://soundcloud.com/',
            'https://sourceforge.net/u/',
            'https://soylentnews.org/~',
            'https://www.sparkpeople.com/mypage.asp?id=',
            'https://speedrun.com/user/',
            'https://splits.io/users/',
            'https://open.spotify.com/user/',
            'https://robertsspaceindustries.com/citizens/',
            'https://steamcommunity.com/groups/',
            'https://steamid.uk/profile/',
            'https://www.strava.com/athletes/',
            'https://forum.sublimetext.com/u/',
            'https://support.t-mobile.com/people/',
            'https://www.taringa.net/',
            'https://tellonym.me/',
            'https://www.gotinder.com/@',
            'https://www.trakt.tv/users/',
            'https://www.travellerspoint.com/users/',
            'https://trello.com/',
            'https://tripadvisor.com/members/',
            'https://www.twitch.tv/',
            'https://mobile.twitter.com/',
            'https://data.typeracer.com/pit/profile?user=',
            'https://ultimate-guitar.com/u/',
            'https://unsplash.com/@',
            'https://vk.com/',
            'https://vsco.co/',
            'https://forum.velomania.ru/member.php?username=',
            'https://venmo.com/',
            'http://fr.viadeo.com/en/profile/',
            'https://vimeo.com/',
            'https://virgool.io/@',
            'https://www.wattpad.com/user/',
            'https://weheartit.com/',
            'https://forums.whonix.org/u/',
            'http://www.wikidot.com/user:info/',
            'https://www.wikipedia.org/wiki/User:',
            'https://community.windy.com/user/',
            'https://xboxgamertag.com/search/',
            'https://www.zhihu.com/people/',
            'https://akniga.org/profile/',
            'https://allmylinks.com/',
            'https://www.babyblog.ru/user/info/',
            'https://chaos.social/@',
            'https://www.couchsurfing.com/people/',
            'https://www.dailykos.com/user/',
            'http://dating.ru/',
            'https://devrant.com/users/',
            'https://www.drive2.ru/users/',
            'https://community.eintracht.de/fans/',
            'https://www.fixya.com/users/',
            'https://www.fl.ru/users/',
            'https://forum.guns.ru/forummisc/blog/',
            'https://www.forumhouse.ru/members/?username=',
            'https://www.geocaching.com/profile/?u=',
            'https://gfycat.com/@',
            'https://habr.com/ru/users/',
            'https://www.hackster.io/',
            'https://www.hunting.ru/forum/members/?username=',
            'https://imgsrc.ru/main/user.php?user=',
            'http://forum.igromania.ru/member.php?username=',
            'https://www.interpals.net/',
            'https://irecommend.ru/users/',
            'https://ko-fi.com/',
            'https://kwork.ru/user/',
            'https://lab.pentestit.ru/',
            'https://last.fm/user/',
            'https://www.livelib.ru/reader/',
            'https://mastodon.cloud/@',
            'https://mastodon.social/@',
            'https://mastodon.technology/@',
            'https://mastodon.xyz/@',
            'https://www.mercadolivre.com.br/perfil/',
            'https://moikrug.ru/',
            'https://mstdn.io/@',
            'https://www.nairaland.com/',
            'https://note.com/',
            'https://www.opennet.ru/~',
            'https://osu.ppy.sh/users/',
            'https://php.ru/forum/members/?username=',
            'https://pikabu.ru/@',
            'https://pr0gramm.com/api/profile/info?name=USERNAME',
            'https://prog.hu/azonosito/info/',
            'https://echo.msk.ru/users/',
            'https://satsis.info/user/',
            'https://social.tchncs.de/@',
            'https://spletnik.ru/user/',
            'https://www.svidbook.ru/user/',
            'http://uid.me/'
        ]

        target = input("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget\u001b[38;5;50m\u001b[38;5;51m]═>\u001b[38;5;7m ")

        for i in URLS:
            try:
                s = urlopen(i + target)
                print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;48m[Tar\u001b[38;5;49mget \u001b[38;5;50mFound\u001b[38;5;51m]═>\u001b[38;5;7m " + str(i))
                with open(f'{target}.txt', 'a') as d:
                    d.write(str(i) + str(target) + "\n")

            except:
                print("\u001b[38;5;46m╚\u001b[38;5;47m══\u001b[38;5;1m[Tar\u001b[38;5;160mget not \u001b[38;5;1mFound\u001b[38;5;160m]═>\u001b[38;5;7m " + str(i))

    elif a == "6":
        print("Welcome to my Proxy Checker! \n")
        
        api = 'http://icanhazip.com'

        proxyfile = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files!", ".")), title="Please chose your ProxyList!")

        try:
            with open(proxyfile, 'r') as proxie:
                prx = proxie.readlines()
                for x in prx:
                    proxy = x.rstrip()

                    try:
                        r = requests.get(api, proxies={'http': 'http://' + proxy}, timeout=1)  
                        if r.status_code == 200:
                            print(f'{Fore.LIGHTGREEN_EX}[+] {proxy}')

                            with open('proxyhits.txt', 'a') as l:
                                l.write(proxy + "\n")

                    except:
                        print(f'{Fore.RED}[-] {proxy}')

        except:
            print("No file found!")


    else:
        Youtube()


ResetTool()