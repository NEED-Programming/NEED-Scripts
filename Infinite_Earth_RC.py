###################### Infinite Air Runecrafting  ############
######################## created by NEED #####################
# Instructions:
# Start at varrock East bank, furthest west stall.
# Click bank stall to ensure proper placement
# Face north, pan above and zoom all the way out
# Start with earth tiara equipped and inventory full of Ess
#  TURN RUN OFF
import random
import time
import pyautogui

########### script ##################

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
        pyautogui.click(button='left', x=502, y=39, duration = 2)
        timetowait = random.randint(3, 6)
        time.sleep(timetowait)

        # Walk to earth altar
        pyautogui.click(button='left', x=747, y=75, duration = 2)
        timetowait = random.randint(14, 16)
        time.sleep(timetowait)

        # Walk to earth altar
        pyautogui.click(button='left', x=750, y=100, duration = 5)
        timetowait = random.randint(14, 16)
        time.sleep(timetowait)

        # Walk to earth altar
        pyautogui.click(button='left', x=698, y=41, duration = 5)
        timetowait = random.randint(15, 17)
        time.sleep(timetowait)

        # Walk to earth altar
        pyautogui.click(button='left', x=704, y=42, duration = 5)
        timetowait = random.randint(15, 17)
        time.sleep(timetowait)

        # Enter mysterious altar
        pyautogui.click(button='left', x=560, y=158, duration = 5)
        timetowait = random.randint(5, 8)
        time.sleep(timetowait)

        # Click craft rune altar
        pyautogui.click(button='left', x=400, y=107, duration = 5)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)

        # incase you lvl
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(2)
        pyautogui.keyDown("space")
        pyautogui.keyUp("space")
        time.sleep(1)

        # Click portal
        pyautogui.doubleClick(button='left', x=335, y=448, duration = 5)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)

        # Walk to bank
        pyautogui.click(button='left', x=651, y=167, duration = 6)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)

        # Walk to bank
        pyautogui.click(button='left', x=653, y=168, duration = 8)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)

        # Walk to bank
        pyautogui.click(button='left', x=676, y=173, duration = 10)
        timetowait = random.randint(10, 12)
        time.sleep(timetowait)

        # walk to BANK
        pyautogui.click(button='left', x=617, y=119, duration = 8)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)
        # WALK TO BANK
        pyautogui.click(button='left', x=78, y=403, duration = 8)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)
        # click bank stall
        pyautogui.click(button='left', x=364, y=303, duration = 8)
        timetowait = random.randint(8, 10)
        time.sleep(timetowait)


