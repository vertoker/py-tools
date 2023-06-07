import mouse
import keyboard
from playsound import playsound

import ctypes
import time as t
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

# This script special create for specific process of crafting
# In that actions script use 9 stacks of gold and 8 stacks of melons
# to create 2 enchanted golden melon and stack of golden melon

timeBetweenMoveAndPress = 0.2
timeClickHandle = 0.2
timeCraftGrabHandle = 0.2
timeAfterCraftGrabHandle = 0.6

fps = 200
pos_mouse_offset_frames = 130
pos_mouse_offset_speed = 1

stopKey = "space"
def sleep(time):
    if keyboard.is_pressed(stopKey):
        exit(0)
    t.sleep(time)
    if keyboard.is_pressed(stopKey):
        exit(0)

# length = 9:1, 0:8
def get_quickbar_pos(pos_x):
    start_pos = (816, 729)
    end_pos = (1105, 729)
    delta_x = (end_pos[0] - start_pos[0]) / 8
    return start_pos[0] + delta_x * pos_x, start_pos[1]

# length = 9:3, 0:8 ; 0:2
def get_invertory_pos(pos_x, pos_y):
    start_pos = (816, 613)
    end_pos = (1105, 685)
    delta_x = (end_pos[0] - start_pos[0]) / 8
    delta_y = (end_pos[1] - start_pos[1]) / 2
    return start_pos[0] + delta_x * pos_x, start_pos[1] + delta_y * pos_y

# length = 3:3, 0:2 ; 0:2
def get_craft_pos(pos_x, pos_y):
    start_pos = (852, 407)
    end_pos = (925, 480)
    delta_x = (end_pos[0] - start_pos[0]) / 2
    delta_y = (end_pos[1] - start_pos[1]) / 2
    return start_pos[0] + delta_x * pos_x, start_pos[1] + delta_y * pos_y

# length = 9:6, 0:8 ; 0:5
def get_chest_pos(pos_x, pos_y):
    start_pos = (816, 371)
    end_pos = (1103, 552)
    delta_x = (end_pos[0] - start_pos[0]) / 8
    delta_y = (end_pos[1] - start_pos[1]) / 5
    return start_pos[0] + delta_x * pos_x, start_pos[1] + delta_y * pos_y

def get_craft_result_pos(handle):
    sleep(handle)
    return 996, 442

# click mouse
def click(pos):
    mouse.move(pos[0], pos[1])
    sleep(timeBetweenMoveAndPress)
    mouse.click(mouse.LEFT)
    sleep(timeClickHandle)

def main_crafter():
    print("Start crafting")
    keyboard.press("shift")
    for i in range(8):
        click(get_quickbar_pos(i))
        click(get_craft_result_pos(timeCraftGrabHandle))
        sleep(timeAfterCraftGrabHandle)
        
        click(get_quickbar_pos(i))
        click(get_invertory_pos(0, 0))
        click(get_invertory_pos(1, 0))
        click(get_invertory_pos(2, 0))
        click(get_invertory_pos(i, 2))#
        click(get_invertory_pos(3, 0))
        click(get_invertory_pos(4, 0))
        click(get_invertory_pos(5, 0))
        click(get_invertory_pos(6, 0))
        click(get_craft_result_pos(timeCraftGrabHandle))
        sleep(timeAfterCraftGrabHandle)
    
    click(get_invertory_pos(7, 0))
    click(get_invertory_pos(8, 0))
    click(get_invertory_pos(0, 1))
    click(get_invertory_pos(1, 1))
    click(get_invertory_pos(8, 2))#
    click(get_invertory_pos(2, 1))
    click(get_invertory_pos(3, 1))
    click(get_invertory_pos(4, 1))
    click(get_invertory_pos(5, 1))
    click(get_craft_result_pos(timeCraftGrabHandle))
    sleep(timeAfterCraftGrabHandle)
    
    print("Get result")
    for i in range(8):
        click(get_quickbar_pos(i))
    click(get_invertory_pos(0, 0))
    click(get_craft_pos(1, 1))
    click(get_craft_result_pos(timeCraftGrabHandle))
    
    keyboard.release("shift")
    sleep(0.5)
    
    playsound("E:\Projects\Python\PyTools\HypixelTools\Success.wav")

def pull_items(count):
    keyboard.press("shift")
    
    for i in range(count):
        click(get_chest_pos(i, 0))
    
    keyboard.release("shift")
    #sleep(0.5)

def push_items():
    keyboard.press("shift")
    
    click(get_quickbar_pos(0))
    click(get_quickbar_pos(7))
    
    keyboard.release("shift")
    #sleep(0.5)

def craft_cycle(cycles):
    for i in range(cycles):
        for i in range(pos_mouse_offset_frames):
            mouse.move(960 + pos_mouse_offset_speed, 540)
            sleep(1 / fps)
        
        mouse.click(mouse.RIGHT)
        sleep(0.8)
        pull_items(8)
        keyboard.press("esc")
        keyboard.release("esc")
        
        for i in range(pos_mouse_offset_frames * 2):
            mouse.move(960 - pos_mouse_offset_speed, 540)
            sleep(1 / fps)
        
        mouse.click(mouse.RIGHT)
        sleep(0.8)
        pull_items(9)
        keyboard.press("esc")
        keyboard.release("esc")
        
        for i in range(pos_mouse_offset_frames):
            mouse.move(960 + pos_mouse_offset_speed, 540)
            sleep(1 / fps)
        
        keyboard.press("9")
        keyboard.release("9")
        sleep(0.3)
        mouse.click(mouse.RIGHT)
        sleep(1)
        click(get_chest_pos(4, 3))
        sleep(1)
        main_crafter()
        keyboard.press("esc")
        keyboard.release("esc")
        sleep(0.5)
        keyboard.press("1")
        keyboard.release("1")
        
        for i in range(pos_mouse_offset_frames):
            mouse.move(960, 540 + pos_mouse_offset_speed)
            sleep(1 / fps)
        
        mouse.click(mouse.RIGHT)
        sleep(0.8)
        push_items()
        keyboard.press("esc")
        keyboard.release("esc")
        
        for i in range(pos_mouse_offset_frames):
            mouse.move(960, 540 - pos_mouse_offset_speed)
            sleep(1 / fps)

        for i in range(50):
            sleep(1)
    
    playsound("E:\Projects\Python\PyTools\HypixelTools\Success.wav")

print("Wait 5 sec")
sleep(5)

craft_cycle(2)
#main_crafter()
