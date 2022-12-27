import pyautogui
import time

# Sleeping the script so we have time to set the mouse on its position
time.sleep(3)

# Getting the mouse position
print(pyautogui.position())

# 1 (loop): Point(x=408, y=61)
# 1 (stop): Point(x=319, y=60)