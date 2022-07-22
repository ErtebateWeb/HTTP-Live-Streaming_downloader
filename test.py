import subprocess

# url = "https://www.mongard.ir/courses/django-beginners/episode/858/django-beginners-forms/"

# name = url.split('/')[-2]
# print(name)
# id= url.split('/')[-3]
# print(id)

cmd= "C:/Users/HP/Downloads/Compressed/VLC/vlc.exe -I dummy -vvv https://mongard.arvanvod.com/ZbKXkQ4RvJ/9O0gxJr6lB/h_,1080_1200,k.mp4.list/index-f1-v1-a1.m3u8 --sout=#transcode{vcodec=h264,vb=1200,acodec=mp4a,ab=192,channels=2,deinterlace}:standard{access=file,mux=ts,dst=1-216-django-beginners-intro.mp4}"
list=cmd.split(' ')
print(list) 

subprocess.Popen(list)