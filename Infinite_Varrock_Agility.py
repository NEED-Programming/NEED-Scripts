# Gnome Agility Course by NEED
# ensure run is ON
# HAVE ROOFS OFF
# Face North with zoom all the way out and pan up overhead.
# enjoy!

import time
import random
import pyautogui



pyautogui.moveTo(0, 1, duration = 1.2)
pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

while True:


    # Clothing line
    pyautogui.click(button='left', x=286, y=278, duration = 3)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)


    # leap gap
    pyautogui.click(button='left', x=257, y=237, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)


    # balance wall
    pyautogui.click(button='left', x=295, y=285, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)


    # Leap Gap
    pyautogui.click(button='left', x=436, y=358, duration = 6)
    timetowait = random.randint(7, 10)
    time.sleep(timetowait)


    # leap gap
    pyautogui.click(button='left', x=631, y=262, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)

    # leap gap
    pyautogui.click(button='left', x=610, y=230, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)

    # hurddle ledge
    pyautogui.click(button='left', x=412, y=188, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)

    # jump off ledge
    pyautogui.click(button='left', x=413, y=206, duration = 6)
    timetowait = random.randint(8, 10)
    time.sleep(timetowait)

    # rough wall
    pyautogui.click(button='left', x=113, y=317, duration = 6)
    timetowait = random.randint(5, 7)
    time.sleep(timetowait)

