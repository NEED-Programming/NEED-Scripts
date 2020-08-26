# infinite Cannon Ball Smither by NEED
# start ANYWHERE but must have Amulet of Glory equipped and worn equipment closed
# Face North, pan all the way out and be overhead
# steel Bars must be top left in tab with mold next to it. Ensure ball(s) is in the 3rd slot on top row.
# Make sure inventory is closed.
# start script and enjoy :)

import random
import time
import pyautogui

pyautogui.moveTo(0, 0, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False


# left click worn equipment tab
pyautogui.click(button='left', x=681, y=468, duration = 3.5)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# right click glory
pyautogui.click(button='right', x=663, y=248, duration = 3.5)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# left click edgeville
pyautogui.click(button='left', x=573, y=289, duration = 3.2)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# left click worn equipment
pyautogui.click(button='left', x=681, y=468, duration = 3.4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click bank
pyautogui.click(button='left', x=545, y=320, duration = 4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click All
pyautogui.moveTo(349, 343, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=349, y=343, duration = 4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click placeholder
pyautogui.moveTo(379, 336, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=379, y=336, duration = 3)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click cannon mold
pyautogui.moveTo(150, 115, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=150, y=115, duration = 3)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click steel bars
pyautogui.moveTo(102, 120, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=102, y=120, duration = 2)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

#click close bank
pyautogui.moveTo(502, 40, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=502, y=40, duration = 2)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# click furnace
pyautogui.moveTo(587, 200, 3, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=587, y=200, duration = 4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)
# Random time for anti-ban
print("Random integer from 1 to 3")
num1 = random.randint(1, 3)
print("Random integer: ", num1)

# click all
pyautogui.moveTo(352, 341, 1, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=483, y=391, duration = 4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)

# Create Cannon Ball
pyautogui.moveTo(255, 466, 1, pyautogui.easeInOutQuad)
pyautogui.click(button='left', x=255, y=446, duration = 4)
timetowait = random.randint(3, 6)
time.sleep(timetowait)
# Random time for anti-ban
print("Random integer from 136 to 140")
num1 = random.randint(136, 140)
print("Random integer: ", num1)
time.sleep(num1)

while True:

    # Click bank
    pyautogui.moveTo(128, 370, 3, pyautogui.easeInOutQuad)
    pyautogui.click(button='left', x=128, y=370, duration = 4)
    timetowait = random.randint(1, 3)
    time.sleep(timetowait)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

    #click steel bars
    pyautogui.moveTo(105, 117, 3, pyautogui.easeInOutQuad)
    pyautogui.click(button='left', x=105, y=117, duration = 4)
    timetowait = random.randint(1, 3)
    time.sleep(timetowait)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

    #close bank
    pyautogui.moveTo(501, 42, 2, pyautogui.easeInOutQuad)
    pyautogui.click(button='left', x=501, y=42, duration=4)
    timetowait = random.randint(1, 3)
    time.sleep(timetowait)
    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)
    time.sleep(num1)

    # click furnace
    pyautogui.moveTo(587, 200, 3, pyautogui.easeInOutQuad)
    pyautogui.click(button='left', x=587, y=200, duration=4)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)

    # Create Cannon Ball
    pyautogui.moveTo(255, 466, 3, pyautogui.easeInOutQuad)
    pyautogui.click(button='left', x=255, y=446, duration=4)
    timetowait = random.randint(3, 6)
    time.sleep(timetowait)
    # Random time for anti-ban
    print("Random integer from 136 to 140")
    num1 = random.randint(136, 140)
    print("Random integer: ", num1)
    time.sleep(num1)
