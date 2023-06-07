from moviepy.editor import *
from pytube import YouTube
import numpy as np
import os

# Скачиваем видео
link = input('Введите ссылку на видео: ')
yt = YouTube(link)
print('Начало загрузки')
path = os.path.join(os.getcwd(), '.output')
yt.streams.first().download(path, 'video')
print('Загрузка завершена')

# Выделяем аудио
videopath = os.path.join(path, 'video.mp4')
audiopath = os.path.join(os.getcwd(), '.audio.wav')
clip = VideoFileClip(videopath)
clip.audio.write_audiofile(audiopath)

input('Конец программы\nНажмите Enter')
