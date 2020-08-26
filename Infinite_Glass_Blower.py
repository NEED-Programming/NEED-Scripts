# Infinite Glass Blower by NEED#
# Directions#
# must be at varrock west bank, southern most stall
# Glass must be in first slot and glassblowing pipe must be to the right of it.
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

#  Right Click Blowpipe
pyautogui.click(button='right', x=123, y=114, duration = 3.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# Left click 1 blowpipe
pyautogui.click(button='left', x=57, y=157, duration = 5)
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

# Click Molten GLass
pyautogui.click(button='left', x=74, y=114, duration = 1.5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

# close bank
pyautogui.click(button='left', x=470, y=37, duration = 3)

# click blowpipe then glass
pyautogui.click(button='left', x=571, y=318, duration = 2.5)
pyautogui.click(button='left', x=611, y=322, duration = 2.5)
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

# click Lantern Lense
pyautogui.click(button='left', x=404, y=518, duration = 2.2)
print("Random integer from 49 to 51")
num1 = random.randint(49, 51)
print("Random integer: ", num1)
time.sleep(num1)

while True:

#click bank
    pyautogui.click(button='left', x=400, y=308, duration = 3)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# click Molten Glass {deposit all}
    pyautogui.click(button='left', x=612, y=322, duration = 3)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# Click Molten Glass
    pyautogui.click(button='left', x=76, y=111, duration = 2.2)
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

# click blowpipe then glass
    pyautogui.click(button='left', x=570, y=315, duration = 2.5)
    pyautogui.click(button='left', x=610, y=321, duration = 2.5)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

# click Space
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    print("Random integer from 49 to 51")
    num1 = random.randint(49, 51)
    print("Random integer: ", num1)
    time.sleep(num1)