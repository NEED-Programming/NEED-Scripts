# Gnome Agility Course by NEED
# ensure run is ON
# HAVE ROOFS OFF
# Face North with zoom all the way out and pan up overhead.
# enjoy!

import time
import random
import pyautogui

pyautogui.moveTo(0, 0, duration = 1)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

# Click starting spot
pyautogui.click(button='left', x=382, y=273, duration = 2)
timetowait = random.randint(3, 6)
time.sleep(timetowait)
# Click log balance
pyautogui.click(button='left', x=382, y=292, duration = 2)
timetowait = random.randint(5, 7)
time.sleep(timetowait)
while True:
    timetowait = random.randint(5, 7)
    time.sleep(timetowait)
    # Climb obstacle net
    pyautogui.click(button='left', x=378, y=337, duration = 2)
    timetowait = random.randint(5, 7)
    time.sleep(timetowait)
# Climb Tree Branch
    pyautogui.click(button='left', x=383, y=284, duration = 4)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# left click Balancing Rope
    pyautogui.click(button='left', x=464, y=275, duration = 2.5)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# Climb down tree
    pyautogui.click(button='left', x=436, y=282, duration = 8)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# Climb Obstacle Net
    pyautogui.click(button='left', x=357, y=184, duration = 4)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# Obstacle Pipe
    pyautogui.click(button='left', x=366, y=209, duration = 4)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# click log
    pyautogui.click(button='left', x=221, y=296, duration = 10)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)