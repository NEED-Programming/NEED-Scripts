# Infinite Jug of Wine Maker by NEED#
# Directions#
# must be at varrock west bank, southern most stall
# Ingredient must be in first slot and unfinished potion must be to the right of it.
# ensure you have withdraw X set to 14
# Zoom all the way out and face north
# Make sure inventory is open
# start script and enjoy :)

import random
import time
import pyautogui

pyautogui.moveTo(0, 1, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

#click bank
pyautogui.click(button='left', x=400, y=308, duration = 2)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
#right click quantity
pyautogui.click(button='right', x=295, y=413, duration = 2)
pyautogui.click(button='left', x=278, y=459, duration = 2)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
#left set custom  quantity
pyautogui.keyDown("1")
pyautogui.keyUp("1")
pyautogui.keyDown("4")
pyautogui.keyUp("4")
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
# Click grape
pyautogui.click(button='left', x=77, y=114, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
# Click jug of water
pyautogui.click(button='left', x=122, y=114, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
# close bank
pyautogui.click(button='left', x=472, y=39, duration = 1.5)
# click grape then jug of water
pyautogui.click(button='left', x=613, y=428, duration=1.5)
pyautogui.click(button='left', x=654, y=426, duration=1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
# click All
pyautogui.click(button='left', x=474, y=459, duration = 2.2)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)
# click to make jug of wine
pyautogui.click(button='left', x=239, y=520, duration = 2.2)
print("Random integer from 18 to 19")
num1 = random.randint(18, 19)
print("Random integer: ", num1)
time.sleep(num1)

while True:
#click bank
    pyautogui.click(button='left', x=391, y=307, duration = 2)
    print("Random integer from 1 to 2")
    num1 = random.randint(1, 2)
    print("Random integer: ", num1)
    time.sleep(num1)
# click on wine
    pyautogui.click(button='left', x=572, y=326, duration = 2)
    # Random time for anti-ban
    print("Random integer from 1 to 2")
    num1 = random.randint(1, 2)
    print("Random integer: ", num1)
    time.sleep(num1)
# Click grape
    pyautogui.click(button='left', x=74, y=114, duration = 2.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# Click jug of water
    pyautogui.click(button='left', x=126, y=114, duration = 1)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# close bank
    pyautogui.click(button='left', x=472, y=38, duration = 1.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# click grape then jug of water
    pyautogui.click(button='left', x=613, y=428, duration = 1.2)
    pyautogui.click(button='left', x=654, y=426, duration = 1.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 2)
    print("Random integer: ", num1)
    time.sleep(num1)
# click to make potion
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")
    print("Random integer from 18 to 19")
    num1 = random.randint(18, 19)
    print("Random integer: ", num1)
    time.sleep(num1)