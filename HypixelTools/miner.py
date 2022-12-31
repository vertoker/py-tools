import mouse
import keyboard
from playsound import playsound

import ctypes
import time
import os

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    print("For work program must have administration rights")
    print("Launch script as administrator\n")
    input("Press Enter to exit...")
    exit(0)

# Example usage
# end world : -647 -247 or -613 103 -173 : 42.2 : 11 : 60
# dwarves mines : 62 -118 : 22.7 : 35 : 120

speedMoveAround = -11
timeExecute = 5 * 60 * 60
frameRate = 60
stopKey = "space"

# Actions here
print("Wait 10 sec")
time.sleep(10)

print("Start mining")
mouse.press("left")
time.sleep(0.5)
for i in range(frameRate * timeExecute):
    mouse.move(959 + speedMoveAround, 540)
    time.sleep(1 / frameRate)
    if keyboard.is_pressed(stopKey):
        break
time.sleep(0.5)
mouse.release("left")
print("End mining")

playsound("E:\Projects\Python\PyTools\HypixelTools\Success.wav")
