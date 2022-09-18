import pyautogui
import time

# Sleeping the script so we have time to set the mouse on its position
time.sleep(10)

# Getting the mouse position
print(pyautogui.position())