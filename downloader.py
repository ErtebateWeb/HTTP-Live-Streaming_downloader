from datetime import date
from inspect import _void
import requests
from bs4 import BeautifulSoup
import sys
import os
import subprocess

import json
# a python program to get tre courses link from the website and save it in a json file then download the courses and convert them with vlc
# the link is https://www.mongard.ir/courses/

# url = "https://www.mongard.ir/courses/"
site="https://www.mongard.ir"
url = "https://www.mongard.ir/courses/python-beginner-course/"

request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
title = soup.title.text

# links= soup.find_all('a', class_='course_link')
links= soup.find_all('a', class_='episode_link')
# data = data[1:]
print(title)
# print(links)
# print(res.get_text())
i=1
for link in links:
    # name=link.find('div', attrs={'class':'_3wU53n'})
    # print(link)
    episode_url=link.get('href')
    # print(f"{site}{episode_url}")
    episode_link=requests.get(f"{site}{episode_url}")
    # print("episode_link",episode_link.url)
    episode=BeautifulSoup(episode_link.content, 'html.parser')
    video_iframe=episode.find('iframe')
    video_link=video_iframe.get('src')
    # print("video link=",video_link)
    splited_url=video_link.split('=')
    video_id=splited_url[1]
    epl=str(episode_link.url)
    name = epl.split('/')[-2]
    # print(name)
    id= epl.split('/')[-3]
    # print(id)
    video_id=video_id.replace('origin_config.json','h_,1080_1200,k.mp4.list/index-f1-v1-a1.m3u8')
    # print("video_id=",video_id)
    # https://mongard.arvanvod.com/WXoB7mjqNk/1ka6q27DzZ/h_,1080_1200,k.mp4.list/index-f1-v1-a1.m3u8
    arg = f" -I dummy -vvv {video_id} --sout=#transcode{{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}}:standard{{access=file,mux=ts,dst={i}-{id}-{name}.mp4}}"
    i+=1
    # print(arg)
    vlc= "C:/Users/HP/Downloads/Compressed/VLC/vlc.exe" + arg
    # print(vlc)
    list=vlc.split(' ')
    p=  subprocess.Popen(list)
    # subprocess.Popen([vlc])
    # p = subprocess.Popen([os.path.join("C:/", "Users", "HP", "Downloads", "Compressed","VLC","vlc.exe "), arg])







# vlc
#vlc.exe -I dummy -vvv <file_URL> --sout=#transcode{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}:standard{access=file,mux=ts,dst=<filename>.mp4