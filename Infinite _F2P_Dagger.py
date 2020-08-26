# f2p Bronze smithing bot#
# Directions#
# must be at varrock west bank, southern most stall
# Hammer must be in first slot in inventory. Corresponding Bars must be top left to right of bank in a row
# open and close bank to ensure you are on the correct tile. 2nd Zoom from the left
# Face north, and pan all the way to above view
# Make sure inventory is closed and full of bronze bars
# start script and enjoy :)

import random
import time
import pyautogui


pyautogui.moveTo(0, 0, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

# anvil
pyautogui.click(button='left', x=442, y=462, duration = 3.8)
time.sleep(1.2)
# CLick All
pyautogui.click(button='left', x=494, y=259, duration = 3.8)

# Bronze Dagger
pyautogui.click(button='left', x=50, y=80, duration = 5.2)

# Random time for anti-ban
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

# return to bank
pyautogui.click(button='left', x=355, y=144, duration = 71.50)
time.sleep(2)
# click deposit all
pyautogui.click(button='left', x=346, y=338, duration = 6.0)
# Random time for anti-ban
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)
time.sleep(num1)

while True:
# click deposit
    pyautogui.click(button='left', x=642, y=200, duration = 4)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# click bar
    pyautogui.click(button='left', x=108, y=114, duration = 1.50)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# close bank
    pyautogui.click(button='left', x=504, y=35, duration = 1.50)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
# anvil
    pyautogui.click(button='left', x=442, y=459, duration = 3.8)
# Bronze Dagger
    pyautogui.click(button='left', x=50, y=80, duration = 5.2)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
    # return to bank
    pyautogui.click(button='left', x=355, y=144, duration = 71.50)
    time.sleep(2)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)
