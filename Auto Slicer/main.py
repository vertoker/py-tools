import threading as th
import easygui as gui2
import pyperclip as clipboard
import PySimpleGUI as gui
import random as rnd

import staticdata
import render

data = [
	[rnd.randint(1000000000, 9999999999), (1920, 1080), 'G:\\Projects\\Python\\AutoSlicer\\test data\\result.mp4'],
	[
		['G:\\Projects\\Python\\AutoSlicer\\test data\\source1.mp4',
		True, True, True, True, 3, 20, 0, 1963, 0]
	],
	['G:\\Projects\\Python\\AutoSlicer\\test data\\audio.mp3', 0, 0, 0, 0]
]

updated = False
gui.theme('DarkAmber')
window = gui.Window('Auto Slicer', staticdata.layout)
event, values = window.read()

def logger(message):
	window['logger'].update(value = message)

def renderVideo():
	render.renderVideo(logger)
	global updated
	updated = False

def updateAll():
	languageUpdate()
	seedUpdate()
	resolutionUpdate()
	videoPathUpdate()
	audioPathUpdate()
	videoResultPathUpdate()

def languageUpdate():
	global values
	index = staticdata.languages.index(values['language_select'])
	for key, value in staticdata.language_data.items():
		window[key].update(value[index])
	solution_combo = staticdata.video_solution[index]
	window['video_solution_select'].update(values=solution_combo.Values)

def seedUpdate():
	global data
	window['seed_text'].update(data[0][0])

def resolutionUpdate():
	global data
	window['video_resolution_width'].update(data[0][1][0])
	window['video_resolution_heigth'].update(data[0][1][1])
	window['video_resolution_select'].update(str(data[0][1][0]) + 'x' + str(data[0][1][1]))

def videoPathOpen():
	try:
		open(gui2.fileopenbox(default = data[1][0][0] + '.mp4'), 'w').write(data[1][0][0])
	except:
		pass
	videoPathUpdate()

def audioPathOpen():
	try:
		open(gui2.fileopenbox(default = data[2][0] + '.mp3'), 'w').write(data[2][0])
	except:
		pass
	audioPathUpdate()

def videoResultPathOpen():
	try:
		open(gui2.filesavebox(default = data[0][2] + '.mp4'), 'w').write(data[0][2])
	except:
		pass
	videoResultPathUpdate()

def videoPathUpdate():
	window['video_path_input'].update(data[1][0][0])

def audioPathUpdate():
	window['audio_path_input'].update(data[2][0])

def videoResultPathUpdate():
	window['result_video_path_input'].update(data[0][2])

updateAll()


while True:
	event, values = window.read()
	#print(event, values) #debug
	if not updated:
		if event in (gui.WINDOW_CLOSED, "-ESCAPE-"):
			break
		if event == 'render':
			updated = True
			updater = th.Thread(target = renderVideo)
			updater.start()
		# Основное
		if event == 'language_select':
			languageUpdate()
		if event == 'seed_refresh':
			data[0][0] = rnd.randint(1000000000, 9999999999)
			seedUpdate()
			logger('Text refreshed')
		if event == 'seed_copy':
			clipboard.copy(data[0][0])
			logger('Text copied')
		if event == 'video_resolution_width':
			data[0][1] = (values['video_resolution_width'], values['video_resolution_heigth'])
			resolutionUpdate()
		if event == 'video_resolution_heigth':
			data[0][1] = (values['video_resolution_width'], values['video_resolution_heigth'])
			resolutionUpdate()
		if event == 'video_resolution_select':
			data[0][1] = values['video_resolution_select'].split('x')
			resolutionUpdate()
		# Видео
		if event == 'video_path_button':
			videoPathOpen()
		if event == 'video_path_input':
			data[1][0][0] = values['video_path_input']
		if event == 'video_slice_checkbox':
			data[1][0][1] = values['video_slice_checkbox']
		if event == 'audio_mute_checkbox':
			data[1][0][2] = values['audio_mute_checkbox']
		if event == 'shuffle_separately_checkbox':
			data[1][0][3] = values['shuffle_separately_checkbox']
		if event == 'shuffle_in_general_checkbox':
			data[1][0][4] = values['shuffle_in_general_checkbox']
		if event == 'min_slice_length_input':
			data[1][0][5] = values['min_slice_length_input']
		if event == 'max_slice_length_input':
			data[1][0][6] = values['max_slice_length_input']
		if event == 'start_video_input':
			data[1][0][7] = values['start_video_input']
		if event == 'end_video_input':
			data[1][0][8] = values['end_video_input']
		# Аудио
		if event == 'audio_path_button':
			audioPathOpen()
		if event == 'result_video_path_button':
			videoResultPathOpen()
		if event == '':
			pass
