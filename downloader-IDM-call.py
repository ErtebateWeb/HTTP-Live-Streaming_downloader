from datetime import date
from inspect import _void
from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
import os
import subprocess
import config
# from idm import IDMan
import json
from subprocess import call
IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

def IDM_download(i,video_url,episode_url,course_title):
    episode_title=episode_url.split('/')[-2]
    episode_id=episode_url.split('/')[-3]
    course_title_en=episode_url.split('/')[-5]
    # print(episode_title)
    # print(episode_id)
    # print(course_title_en)

    # downloader = IDMan()
    url=str(video_url)
    # url = "https://mongard.arvanvod.com/oy1xeb8BG0/Db4oaL9rNv/origin_Z0JPphkx0GqtJXfg4mDc6mS3JPQdg7VdHCLM5v2E.mp4"
    output=f"{i}-{course_title_en}-{episode_id}-{episode_title}.mp4"
    # flag=2
    # downloader.download(url, f"c:\DOWNLOADS\{course_title}", output=output, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag =None , clip=False)
    call([IDM, '/d',video_url, '/p',f"c:\DOWNLOADS\{course_title}", '/f', output, '/n', '/a'])



for p in range(1,4):
        
    site="https://www.mongard.ir"
    page_url = f"https://www.mongard.ir/courses/?page={p}"
    request_page = requests.get(page_url, cookies=config.cookies, headers=config.headers)
    soup_page = BeautifulSoup(request_page.text, 'html.parser')
    # course_title = soup.title.text
    # course_title = soup.find('h1', 'course_top_title').get_text()
    # links= soup.find_all('a', class_='course_top_title')
    # print('course_title=',course_title)
    course_links= soup_page.find_all('a', class_='course_link')
    
    for course_link in course_links:
        print (site+course_link.get('href'))
    
        course_url = site+course_link.get('href')
        # course_url = input("Please enter course url:")

        request = requests.get(course_url, cookies=config.cookies, headers=config.headers)
        soup = BeautifulSoup(request.text, 'html.parser')
        # course_title = soup.title.text
        course_title = soup.find('h1', 'course_top_title').get_text()
        # links= soup.find_all('a', class_='course_top_title')
        # print('course_title=',course_title)
        links= soup.find_all('a', class_='episode_link')
        # print('links=',links)
        i=0
        for link in links:
            episode_url=site+link.get('href')
            print(episode_url)
            request_episode = requests.get(episode_url, cookies=config.cookies, headers=config.headers)
            episode=BeautifulSoup(request_episode.content, 'html.parser')
            episode_mp4_url=episode.find('source', type="video/mp4").get('src')
            # print(episode_mp4_url)    
            IDM_download(i,episode_mp4_url,episode_url,course_title)
            i+=1