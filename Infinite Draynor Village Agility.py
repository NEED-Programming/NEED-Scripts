# Draynor Agility Course by NEED
# ensure run is ON
# HAVE ROOFS OFF
# close inventory
# Face North with zoom all the way out and pan up overhead.
# enjoy!

import time
import random
import pyautogui

pyautogui.moveTo(0, 1, duration = 1.2)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

# left click worn equipment tab
pyautogui.click(button='left', x=681, y=464, duration = 3.5)

# right click glory
pyautogui.click(button='right', x=662, y=242, duration = 3.5)

time.sleep(2.2)

# left click draynor village
pyautogui.click(button='left', x=585, y=319, duration = 3.2)

# left click worn equipment
pyautogui.click(button='left', x=681, y=468, duration = 3.4)

time.sleep(2.2)

# Run to Wall
pyautogui.click(button='left', x=393, y=98, duration = 7)

time.sleep(3.8)

# Click Rough Wall
pyautogui.click(button='left', x=343, y=133, duration = 6)
time.sleep(2)

while True:

# Click Tightrope 1
    pyautogui.click(button='left', x=314, y=296, duration = 6)

    time.sleep(3)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Tightrope 2
    pyautogui.click(button='left', x=412, y=275, duration = 8)

    time.sleep(3)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Narrow Wall
    pyautogui.click(button='left', x=337, y=307, duration = 8)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Jump wall
    pyautogui.click(button='left', x=380, y=351, duration = 6)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Jump gap
    pyautogui.click(button='left', x=489, y=271, duration = 5)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Climb Down Crate
    pyautogui.click(button='left', x=467, y=198, duration = 8)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Run near wall
    pyautogui.click(button='left', x=415, y=99, duration = 8)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)

# Click Rough wall
    pyautogui.click(button='left', x=336, y=240, duration = 8)

    # Random time for anti-ban
    print("Random integer from 1 to 3")
    num1 = random.randint(1, 3)
    print("Random integer: ", num1)

    time.sleep(num1)