import os, re
import shutil
import time

import requests

from os import path as p
from tkinter import filedialog

from bs4 import BeautifulSoup

# Данные для поиска треков на ПК
start_path = "C:\\Users"
packages_path = "AppData\\Local\\Packages"
ya_music_folder_contains = "Yandex.Music"
saved_tracks = "LocalState\\Music"

ya_music_link = "https://music.yandex.ru/track/"


def find_tracks():
    tracks = []
    path_exists = False
    out_path = start_path
    for user_name in os.listdir(start_path):
        out_path = p.join(start_path, user_name, packages_path)
        if p.exists(out_path):
            path_exists = True
            break

    if not path_exists:
        return "Папка " + packages_path + " не найдена"
    path_exists = False

    for directory in os.listdir(out_path):
        if ya_music_folder_contains in directory:
            out_path = p.join(out_path, directory, saved_tracks)
            if p.exists(out_path):
                path_exists = True
                break

    if not path_exists:
        return "Папка с треками " + out_path + " не найдена"
    path_exists = False

    for directory in os.listdir(out_path):
        out_path = p.join(out_path, directory)

    return out_path


def input_open_folder_name():
    user_input = filedialog.askdirectory()
    if not os.path.isdir(user_input):
        return input_open_folder_name()
    return user_input


def copy_between_directories(file_names, from_directory, to_directory):
    for file_name in file_names:
        shutil.copyfile(p.join(from_directory, file_name), p.join(to_directory, file_name))


def rename_tracks(directory, tracks):
    for track in tracks:
        old_file = p.join(directory, track)
        track_split = track.split('.')
        url = ya_music_link + track_split[0]

        time.sleep(1.5)
        page = requests.get(url)
        print(url)
        if not page.status_code == 200:
            print("Error, code:", page.status_code)
            break

        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.find('div', attrs={'class': 'sidebar__title sidebar-track__title deco-type typo-h2'})
        title = title.find('a', attrs={'class': 'd-link deco-link'}).text
        authors = soup.find('div', attrs={'class': 'sidebar__info sidebar__info-short'})
        if authors is None:
            authors = soup.find('div', attrs={'class': 'sidebar__info'})
            authors = authors.find_all('a', attrs={'class': 'd-link deco-link'})
        else:
            authors = authors.find_all('a', attrs={'class': 'd-link deco-link'})

        authors = ", ".join([author.text for author in authors])
        new_name = title + "- " + authors + '.' + track_split[1]
        new_name = new_name.replace("\\", "")
        new_name = new_name.replace("/", "")
        new_name = new_name.replace(":", "")
        new_name = new_name.replace("*", "")
        new_name = new_name.replace("?", "")
        new_name = new_name.replace("\"", "")
        new_name = new_name.replace("\'", "")
        new_name = new_name.replace("<", "")
        new_name = new_name.replace(">", "")
        new_name = new_name.replace("|", "")
        new_name = new_name.replace("+", "")

        new_file = p.join(directory, new_name)
        os.renames(old_file, new_file)
        print(new_name)


print("Форматирование скачанных треков из Яндекс Музыки")
print()
print("Поиск треков в файлах")
tracks_directory = find_tracks()
tracks = next(os.walk(tracks_directory), (None, None, []))[2]
print("Количество найденных треков:", len(tracks))

print()
print("Введите папку для копирования: ", sep='', end='')
save_directory = input_open_folder_name()
print(save_directory)

print()
print("Копирование треков между директориями")
copy_between_directories(tracks, tracks_directory, save_directory)
print("Копирование завершено")
print("Количество файлов в новой папке:", len(os.listdir(save_directory)))

print()
print("Переименовывание треков")
rename_tracks(save_directory, tracks)
print("Треки готовы")
input("Нажми Enter чтобы закончить")
