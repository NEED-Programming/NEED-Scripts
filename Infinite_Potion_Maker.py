# Infinite Potion Maker by NEED#
# Directions#
# must be at varrock west bank, southern most stall
# Ingredient must be in first slot and unfinished potion must be to the right of it.
# ensure you have withdraw X set to 14
# Zoom all the way out and face north
# Make sure inventory is open
# start script and enjoy :)
# updated: 8/24/2020
import random
import time
import pyautogui

pyautogui.moveTo(0, 0, duration= .5)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False
#click bank
pyautogui.click(button='left', x=395, y=261, duration=4)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

# Click ingredient
pyautogui.click(button='left', x=101, y=112, duration = 5)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

# Click Unfinished potion
pyautogui.click(button='left', x=145, y=115, duration= 2)

# Random time for anti-ban
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

# close bank
pyautogui.click(button='left', x=497, y=38, duration = 3)

# click ingredient then unfinished potion
pyautogui.click(button='left', x=636, y=318, duration=2.5)
pyautogui.click(button='left', x=677, y=315, duration=2.5)

# Random time for anti-ban
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

# click to make potion
pyautogui.click(button='left', x=250, y=445, duration=3)
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

time.sleep(num1)

while True:

#click bank
    pyautogui.click(button='left', x=394, y=268, duration=18)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# click on deposit inventory
    pyautogui.click(button='left', x=448,y=328, duration=3)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click ingredient
    pyautogui.click(button='left', x=96, y=117, duration=2.2)

# Click Unfinished potion
    pyautogui.click(button='left', x=145, y=114, duration=2.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)


# Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# close bank
    pyautogui.click(button='left', x=499, y=38, duration = 2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# click ingredient then unfinished potion
    pyautogui.click(button='left', x=637, y=321, duration=2)
    pyautogui.click(button='left', x=679, y=315, duration=2)

# Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# click to make potion
    pyautogui.click(button='left', x=251, y=449, duration=2.2)
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)




























