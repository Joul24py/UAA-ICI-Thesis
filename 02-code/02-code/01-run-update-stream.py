import pyautogui
import time

x = 0
y = 0

# Sleeping the script so we have time to run the schema and then automatically moves to the indicated position
time.sleep(10)
pyautogui.moveTo(x, y)

#The process will be okay while the mouse keeps on the indicated position 
while(pyautogui.position() == (x, y)):
   pyautogui.click()
   time.sleep(1) # The CSV is getting updated each second