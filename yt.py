import os
from pytube import YouTube
import sys
import time
from colorama import init, Fore

def downloading_animation():
    init()  

    toolbar_width = 40

    # Code By Jiku 
    sys.stdout.write("Downloading: [%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  

    for i in range(toolbar_width):
        time.sleep(0.1)  #Time nibe eta
        if i < toolbar_width * 0.25:
            color = Fore.RED
        elif i < toolbar_width * 0.5:
            color = Fore.YELLOW
        elif i < toolbar_width * 0.75:
            color = Fore.GREEN
        else:
            color = Fore.BLUE
        sys.stdout.write(color + "=")
        sys.stdout.flush()

    sys.stdout.write(Fore.RESET + "] 100%\n")
    print("Download complete!")
logo = ("""
\33[1;92m
▬ \33[1;92m███████   ██   ██ ██   ██  █████        \033[33;1m▬▬▬▬▬▬▬▬▬\33[1;92m
▬ \33[1;92m██        ██   ██ ██   ██ ██   ██      \033[33;1m█ V : 0.1 █\33[1;92m
▬ \33[1;92m███████  ██   ██ ███████ ███████ 
▬ \33[1;92m     ██  ██   ██ ██   ██ ██   ██ 
▬ \33[1;92m███████  ██████ ██   ██ ██   ██ 
▬\033[1;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
\033[1;97m Owner   :            MD ROBIUL ISLAM      █    
\033[1;32m Facebook:            MD ROBIUL ISLAM      █
\033[1;97m Github  :            Robiul2034           █
\033[1;32m Whatsapp:            +8801945635207       █
\033[1;97m Tool    :            YT downloader        █
\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m""")

os.system(" clear")
print(logo)
url = input ("Link : ")
filename = input(" Name: ")
try :
yt = YouTube(url)
except:
print(" Network Error")
try:
mp4 = yt.streams.filter(file_extension='mp4',progressive=True)
d_v = mp4.get_highest_resolution()
except:
print("Some error in resolution")
try:
print("Download Starting.....")
print(f"Name :- {yt.title}")
d_v.download(output_path="/sdcard", filename = filename)
downloading_animation()
print(" Done")
except :
print("Some error")