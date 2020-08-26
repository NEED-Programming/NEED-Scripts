###################### Infinite Air Runecrafting  ############
######################## created by NEED #####################
# Instructions:
# Start at Fally East bank, furthest west stall.
# Click bank stall to ensure proper placement
# Face north, pan above and zoom all the way out
# Start with Air tiara equipped and inventory full of Ess
#  TURN RUN OFF

import time
import random
import pyautogui

pyautogui.moveTo(0, 0, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

# Click Bank
pyautogui.click(button='left', x=382, y=290, duration = 3.8)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# Click All
pyautogui.click(button='left', x=352, y=343, duration = 3.8)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

while True:

    # Click Pure essence
    pyautogui.click(button='left', x=104, y=118, duration = 3)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)

    # Close Bank
    pyautogui.click(button='left', x=505, y=41, duration = 2)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)

    # Walk to air altar
    pyautogui.click(button='left', x=674, y=169, duration = 2)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Walk to air altar
    pyautogui.click(button='left', x=683, y=175, duration = 2)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Walk to air altar
    pyautogui.click(button='left', x=661, y=177, duration = 10)
    timetowait = random.randint(15, 17)
    time.sleep(timetowait)

    # Walk to air altar
    pyautogui.click(button='left', x=663, y=177, duration = 8)
    timetowait = random.randint(15, 17)
    time.sleep(timetowait)

    # Enter mysterious altar
    pyautogui.click(button='left', x=219, y=249, duration = 5)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Click craft rune altar
    pyautogui.click(button='left', x=428, y=220, duration = 5)
    timetowait = random.randint(5, 6)
    time.sleep(timetowait)

    # Click use portal
    pyautogui.click(button='left', x=349, y=336, duration = 3)
    timetowait = random.randint(5, 6)
    time.sleep(timetowait)

    # Walk to bank
    pyautogui.click(button='left', x=721, y=46, duration = 2)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Walk to bank
    pyautogui.click(button='left', x=726, y=50, duration = 2)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Walk to bank
    pyautogui.click(button='left', x=707, y=41, duration = 2)
    timetowait = random.randint(14, 16)
    time.sleep(timetowait)

    # Walk to bank
    pyautogui.click(button='left', x=685, y=38, duration = 4)
    timetowait = random.randint(16, 20)
    time.sleep(timetowait)

    # Click bank stall
    pyautogui.click(button='left', x=435, y=273, duration = 4)
    timetowait = random.randint(6, 8)
    time.sleep(timetowait)
