# Infinite SEED Stealer by NEED#
# Directions#
# execute at western most stall, at southwestern position.
# Face North, default zoom and panned all the way up
# start script and enjoy :)

import random
import time
import pyautogui

pyautogui.moveTo(0, 1, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

time.time_ns()

while True:

#1 Click Seed Stall
    pyautogui.click(button='left', x=406, y=307, duration = 2)

    print("Random integer from 7 to 9")
    num1 = random.randint(9, 10)
    print("Random integer: ", num1)

    time.sleep(num1)

#2 Click Seed Stall
    pyautogui.click(button='left', x=408, y=285, duration=3)

    print("Random integer from 9 to 10")
    num1 = random.randint(9, 10)
    print("Random integer: ", num1)

    time.sleep(num1)

#3 Click Seed Stall
    pyautogui.click(button='left', x=402, y=279, duration = 2)

    print("Random integer from 9 to 10")
    num1 = random.randint(9, 10)
    print("Random integer: ", num1)

    time.sleep(num1)

