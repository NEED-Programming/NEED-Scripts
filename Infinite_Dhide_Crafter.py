# Infinite D'Hide Crafter by NEED#
# Directions#
# must be at varrock west bank, southern most stall
# Needle must be in first slot, thread next to it and tanned hide next to that on the top row.
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
pyautogui.click(button='left', x=396, y=301, duration = 3)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# Click Quantity All
pyautogui.click(button='left', x=320, y=408, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

#  left Click needle
pyautogui.click(button='left', x=75, y=112, duration = 3.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# Click thread
pyautogui.click(button='left', x=124, y=111, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# Click tanned hide
pyautogui.click(button='left', x=172, y=110, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# close bank
pyautogui.click(button='left', x=470, y=37, duration = 3)

# click needle then hide
pyautogui.click(button='left', x=571, y=318, duration = 2.5)
pyautogui.click(button='left', x=656, y=323, duration = 2.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# click All
pyautogui.click(button='left', x=471, y=457, duration = 2.2)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# click chest body
pyautogui.click(button='left', x=128, y=518, duration = 2.2)
print("Random integer from 17 to 19")
num1 = random.randint(17, 19)
print("Random integer: ", num1)
time.sleep(num1)

while True:

#click bank
    pyautogui.click(button='left', x=393, y=306, duration = 3)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# click d'hide body {deposit all}
    pyautogui.click(button='left', x=654, y=320, duration = 3)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# Click Molten Glass
    pyautogui.click(button='left', x=172, y=113, duration = 2.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# close bank
    pyautogui.click(button='left', x=472, y=41, duration = 2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# click needle then tanned hide
    pyautogui.click(button='left', x=570, y=315, duration = 2.5)
    pyautogui.click(button='left', x=656, y=319, duration = 2.5)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# click Space
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print("Random integer from 17 to 19")
    num1 = random.randint(17, 19)
    print("Random integer: ", num1)
    time.sleep(num1)