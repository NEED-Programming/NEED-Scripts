# Infinite High Alcher by NEED#
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

# Click magic tab
pyautogui.click(button='left', x=790, y=539, duration = 2)

print("Random integer from 1 to 2")
num1 = random.randint(1, 2)
print("Random integer: ", num1)

time.sleep(num1)

while True:

# click high alch
    pyautogui.click(button='left', x=777, y=266, duration = num1)

    # Random time for anti-ban
    print("Random integer from 1 to 2")
    num1 = random.randint(1, 2)
    print("Random integer: ", num1)

    time.sleep(num1)

# click noted item
    pyautogui.click(button='left', x=630, y=258, duration = num1)

    # Random time for anti-ban
    print("Random integer from 1 to 2")
    num1 = random.randint(1, 2)
    print("Random integer: ", num1)

    time.sleep(num1)