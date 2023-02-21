from PIL import Image, ImageDraw, ImageGrab
import keyboard
import ctypes
import psutil
import mouse
import time
import os

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def kill_process(name):
    try:
        for proc in psutil.process_iter():
            if proc.name() == name:
                proc.kill()
    except:
        Click(1440, 220, 1)
        Click(1390, 245, 1)
    return

def ChestMenu(xSlot, ySlot, yHeight, handle):
    if yHeight == 6:
        mouse.move(815 + xSlot * 36.25, 360 + ySlot * 36.25)# 815/400 1105/575
    if yHeight == 5:
        mouse.move(815 + xSlot * 36.25, 380 + ySlot * 36.25)# 815/415 1110/560
    if yHeight == 1:
        mouse.move(815 + xSlot * 36.25, 450)# 815/485 1105/485
    time.sleep(0.1)
    mouse.click(mouse.LEFT)
    time.sleep(handle)

def is_chest():
    return GetColorScreen(796, 550) == (198, 198, 198)

def vimeworld_path():
    d = input("Введите путь к ярлыку vimeworld: ")
    q = os.path.isfile(d)
    if not q:
        print("Это не файл")
        d = vimeworld_path()
        return d
    else:
        return d

def vimeworld_started(name):
    q = False
    for proc in psutil.process_iter():
        if proc.name() == name:
            q = True
            break
    if not q:
        time.sleep(1)
        q = vimeworld_started(name)
    return q

def Click(xWigth, yHeight, handle):
    mouse.move(xWigth, yHeight)
    mouse.click(mouse.LEFT)
    time.sleep(handle)

def RightClick(xWigth, yHeight, handle):
    mouse.move(xWigth, yHeight)
    mouse.click(mouse.RIGHT)
    time.sleep(handle)

def Write(text, handle):
    keyboard.write(text)
    time.sleep(handle)

def Press(key, handle):
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(handle)

def GetLogin(count):
    return "здесь должна быть ваша ботовая база никнейма" + str(count)

def GetPassword(count):
    return "здесь должна быть ваша ботовая база паролей" + str(count)

def GetColorScreen(x, y):
    return ImageGrab.grab().load()[x, y]