#  Steel smithing bot#
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

# platebody
pyautogui.click(button='left', x=219, y=245, duration = 5.2)

# Random time for anti-ban
timetowait = random.randint(3, 6)
time.sleep(timetowait)


# return to bank
pyautogui.click(button='left', x=355, y=144, duration = 16)
timetowait = random.randint(3, 6)
time.sleep(timetowait)



# click deposit all
pyautogui.click(button='left', x=346, y=338, duration = 6.0)
# Random time for anti-ban
timetowait = random.randint(3, 6)
time.sleep(timetowait)
while True:
# click deposit
    pyautogui.click(button='left', x=642, y=200, duration = 4)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)

# click bar
    pyautogui.click(button='left', x=108, y=114, duration = 1.50)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# close bank
    pyautogui.click(button='left', x=504, y=35, duration = 1.50)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# anvil
    pyautogui.click(button='left', x=442, y=459, duration = 3.8)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
# plate body
    pyautogui.click(button='left', x=219, y=245, duration = 5.2)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
    # return to bank
    pyautogui.click(button='left', x=355, y=144, duration = 16)
    time.sleep(2)
    # Random time for anti-ban
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
