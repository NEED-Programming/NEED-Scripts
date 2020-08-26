# Infinite Ardy Knight Thief by NEED#
# Directions#
# Can execute at any location
# Noted item must be top left.
# Face North, default zoom and panned all the way up
# start script and enjoy :)

import random
import time
import pyautogui

pyautogui.moveTo(0, 1, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False


#1 Click Ardy Knight
pyautogui.click(button='left', x=401, y=267, duration = 2)

print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)


while True:

#1 Click Ardy Knight
    pyautogui.click(button='left', x=401, y=267, duration = 2)

    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

#2 Click Ardy Knight
    pyautogui.click(button='left', x=347, y=332, duration = 2)

    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)