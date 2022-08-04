from datetime import date
from inspect import _void
from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
import os
import subprocess
import config
from idm import IDMan
import json


def IDM_download(i,video_url,episode_url,course_title):
    episode_title=episode_url.split('/')[-2]
    episode_id=episode_url.split('/')[-3]
    course_title_en=episode_url.split('/')[-5]
    # print(episode_title)
    # print(episode_id)
    # print(course_title_en)

    downloader = IDMan()
    url=str(video_url)
    # url = "https://mongard.arvanvod.com/oy1xeb8BG0/Db4oaL9rNv/origin_Z0JPphkx0GqtJXfg4mDc6mS3JPQdg7VdHCLM5v2E.mp4"
    output=f"{episode_id}-{episode_title}.mp4"
    # flag=2
    downloader.download(url, f"c:\DOWNLOADS\{course_title}", output=output, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag =None , clip=False)




site="https://www.mongard.ir"
url = "https://www.mongard.ir/one_part/?page=1"

request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
title = soup.title.text

links= soup.find_all('a', class_='one_part_link')
print(title)
# print(links)
# print(res.get_text())
i=0
j=15
for link in links[i:j]:
    # print(link)
    episode_url=link.get('href')
    print(f"{site}{episode_url}")
    episode_link=requests.get(f"{site}{episode_url}")
    print("episode_link",episode_link.url)
    episode=BeautifulSoup(episode_link.content, 'html.parser')

    article_link=str(episode_link.url)
    article_id=article_link.split('/')[-3]
    article_name_en=article_link.split('/')[-2]

    article_name=episode.find('h1').text
    dir="one_part/"+str(article_id)+"-"+article_name
    directory="one_part/"+str(article_id)+"-"+article_name+"/"
    article_file=dir+"/"+article_name+".txt"

    os.makedirs(os.path.dirname(article_file), exist_ok=True)
    from pathlib import Path
    article_url=site+link.get('href')
    print(episode_url)
    article_mp4_url=episode.find('source', type="video/mp4").get('src')
    # print(episode_mp4_url)    
    IDM_download(i,article_mp4_url,article_url,article_name)


