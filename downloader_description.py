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
# url = "https://www.mongard.ir/courses/python-beginner-course/"
# url = "https://www.mongard.ir/courses/django-beginners/"
url = "https://www.mongard.ir/one_part/?page="
for page in range(1,11):
    url_page=url+str(page)

    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    title = soup.title.text

    # links= soup.find_all('a', class_='course_link')
    # links= soup.find_all('a', class_='episode_link')
    links= soup.find_all('a', class_='one_part_link')
    # data = data[1:]
    print(title)
    print(links)
    # print(res.get_text())
    i=0
    j=15
    for link in links[i:j]:
        # name=link.find('div', attrs={'class':'_3wU53n'})
        # print(link)
        episode_url=link.get('href')
        # print(f"{site}{episode_url}")
        episode_link=requests.get(f"{site}{episode_url}")
        # print("episode_link",episode_link.url)
        episode=BeautifulSoup(episode_link.content, 'html.parser')
        description = episode.find('article', attrs={'class':'description_container'})
        # description = episode.find('div', attrs={'class':'episode_top_description'})
        description_text = description.get_text()
        # print(description_text)
        article_name=episode.find('h1').text
        # print(article_name.text)
        dir=str(page)+"/"+article_name
        article_file=dir+"/"+article_name+".txt"
        # print(article_file)
        # import os
        # os.makedirs(article_file, exist_ok=True)
        
        os.makedirs(os.path.dirname(dir), exist_ok=True)

        from pathlib import Path
        # import errno

        # if not os.path.exists(os.path.dirname(article_file)):
        #     try:
        #         os.makedirs(os.path.dirname(article_file))
        #     except OSError as exc: #
        #         if exc.errno != errno.EEXIST:
        #             raise
        # Path(str(page)+"/"+article_name).mkdir(parents=True, exist_ok=True)
        with open(article_file, 'w', encoding="utf-8") as f:
            f.write(description_text)

        # video_iframe=episode.find('iframe')
        # video_link=video_iframe.get('src')
        # print("video link=",video_link)
        # splited_url=video_link.split('=')
        # video_id=splited_url[1]
        # epl=str(episode_link.url)
        # name = epl.split('/')[-2]
        # print(name)
        # id= epl.split('/')[-3]
        # # print(id)
        # video_id=video_id.replace('origin_config.json','h_,1080_1200,k.mp4.list/index-f1-v1-a1.m3u8')
        # print("video_id=",video_id)
        # https://mongard.arvanvod.com/WXoB7mjqNk/1ka6q27DzZ/h_,1080_1200,k.mp4.list/index-f1-v1-a1.m3u8
        # arg = f" -I dummy -vvv {video_id} --sout=#transcode{{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}}:standard{{access=file,mux=ts,dst={i}-{id}-{name}.mp4}}"
        # arg = f" -vvv {video_id} --sout=#transcode{{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}}:standard{{access=file,mux=ts,dst={i}-{id}-{name}.mp4}}"
        # i+=1
        # # print(arg)
        # vlc= "C:/Users/HP/Downloads/Compressed/VLC/vlc.exe" + arg
        # # print(vlc)
        # list=vlc.split(' ')
        # # p=  subprocess.Popen(list)








    # vlc
    #vlc.exe -I dummy -vvv <file_URL> --sout=#transcode{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}:standard{access=file,mux=ts,dst=<filename>.mp4
    # for %%a in (*.mp4) do "C:\Program Files (x86)\VideoLAN\VLC\vlc" -I dummy "%%a" --sout=#transcode{acodec=mp3,ab=128,vcodec=dummy}:std{access="file",mux="raw",dst="%%a.mp3"} vlc://quit
    # @"%ProgramFiles%\VideoLAN\VLC\vlc.exe" -vvv "http://86.127.212.113/control/faststream.jpg?stream=mxpeg" --sout "#transcode{vcodec=h264,scale=Automat,scodec=none}:file{dst=C:\\Users\\ACV\\Videos\\rec3.mp4,no-overwrite}" --no-sout-all --sout-keep

