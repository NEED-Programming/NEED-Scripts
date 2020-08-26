# P2P Bronze smithing bot @fishing Trawler
# Made by NEED
# Directions#
# Recommend pre-stamina potion for run to Anvil
# Hammer must be in first slot in inventory. Fill inventory full of bronze bars
# Corresponding Bars must be top left to right of bank in a row
# Make sure inventory is closed and full of bronze bars
# Face North and pan all the way above view
# Use NMZ mini-game teleport
# start script and enjoy :)

import time
import pyautogui
pyautogui.moveTo(0, 1, duration = 0.50)

pyautogui.FAILSAFE = False
pyautogui.failsafecheck = False

# starting spot
pyautogui.click(button='left', x=387, y=306, duration = 4.0)

# Run North-East
pyautogui.click(button='left', x=735, y=58, duration = 4.0)

# Run past Mith ore
pyautogui.click(button='left', x=391, y=33, duration = 10.0)

time.sleep(10)

# run to village
pyautogui.click(button='left', x=741, y=60, duration = 8.0)

time.sleep(10)

# click Anvil
pyautogui.click(button='left', x=762, y=198, duration = 8.0)

time.sleep(10)

while True:

# click dagger
    pyautogui.click(button='left', x=58, y=118, duration = 4)

# click Bank
    pyautogui.click(button='left', x=610, y=329, duration = 83)

# click Quantity All
    pyautogui.click(button='left', x=349, y=409, duration = 6)

# click dagger
    pyautogui.click(button='left', x=646, y=379, duration= 3)

# Click Bronze Bars
    pyautogui.click(button='left', x=107, y=113, duration = 4)

# close bank
    pyautogui.click(button='left', x=502, y=37, duration = 3)

# Click Anvil
    pyautogui.click(button='left', x=137, y=248, duration = 6)

    pyautogui.keyDown('space down')
