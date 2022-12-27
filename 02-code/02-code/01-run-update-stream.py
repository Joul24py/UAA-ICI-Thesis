import pyautogui
import time
import os

x = 319
y = 60

# Sleeping the script so we have time to run the schema and then automatically moves to the indicated position
time.sleep(10)
pyautogui.moveTo(x, y)

TenSecCounter = 0

# The process will be okay while the mouse keeps on the indicated position 
while(pyautogui.position() == (x, y)):
    # Deleting data each 10 seconds
    if TenSecCounter == 10:
        os.remove("data.csv")
        TenSecCounter = 0
    
    # Clicking to reload the CSV
    pyautogui.click()
    
    # Getting the number of lines of the file
    File = open("data.csv")
    j = 0
    for i in File:
        j = j + 1
    print("Líneas = " + str(j))
    File.close()
    
    # The CSV gets updated each second
    print("Tiempo = " + str(TenSecCounter))
    time.sleep(1)
    TenSecCounter = TenSecCounter + 1