from datetime import datetime
import requests, os, random
from bs4 import BeautifulSoup
from tkinter import filedialog

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
alphabet = '1234567890abcdefghigklmnopqrstuvwxyz'

def input_int(comment):
	try:
		num = input(comment)
		return int(num)
	except:
		print('Введено не число')
		return input_int(comment)

def convert_base(num, to_base = 10, from_base = 10):
	if isinstance(num, str):
		n = int(num, from_base)
	else:
		n = int(num)
	if n < to_base:
		return alphabet[n]
	else:
		return convert_base(n // to_base, to_base) + alphabet[n % to_base]

def saveImage(url, pathFolder, counter, time):
	session = requests.Session()
	response = session.get(url, headers = HEADERS)
	soup = BeautifulSoup(response.text, features="lxml")
	image_meta = str(soup.find('meta', {'property': 'og:image'}))
	image_link = image_meta.split("\"")[1]

	image = requests.get(image_link)
	if not os.path.exists(pathFolder):
		os.mkdir(pathFolder)
	path = os.path.join(pathFolder, "img " + time + " " + str(counter) + ".jpg")
	out = open(path, "wb")
	out.write(image.content)
	out.close()

def getRandomID():
	mod = convert_base(str(random.randrange(0, 2176782335)), 36, 10)
	return alphabet[0] * (6 - len(mod)) + mod

def download(count, seed, pathFolder):
	random.Random(seed)
	time = str(datetime.now()).replace(':', ' ').replace('-', ' ')
	print('Начало загрузки')
	for x in range(1, count + 1):
		link = "https://prnt.sc/" + str(getRandomID())
		try:
			saveImage(link, pathFolder, x, time)
			print('Загружено скриншотов: ' + str(x) + ' из ' + str(count))
		except:
			print('Скриншот ' + str(x) + ' не был загружен по причине ошибки')
	print('Все скриншоты загружены')

counter = input_int('Введите количество скриншотов для скачки: ')
seed = input_int('Введите сид (можно любое число): ')
print('Введите папку: ', end = '')
pathFolder = filedialog.askdirectory()
print(pathFolder)
download(counter, seed, pathFolder)
