#%% Libraries
import os
import time
import pyautogui
import pandas

#%% Detect the position of the mouse
def MousePosition(secs = 3):
    # Sleeping the script so we have time to set the mouse on its position
    time.sleep(secs)

    # Getting the mouse position
    print(pyautogui.position())

    # 1 (loop): Point(x=408, y=61)
    # 1 (stop): Point(x=319, y=60)
    # 2 (loop): Point(x=512, y=81)
    # 2 (stop): Point(x=399, y=79)
    return

#%% Run a live stream to update the dataset while streaming
def RunUpdateStream(xStop = 319, yStop = 60, xWindow = 319, yWindow = 8, timerRefresher = 1):
    # 1: RunUpdateStream()
    # 2: RunUpdateStream(399, 79, 399, 5, 1)
    
    # Sleeping the script so we have time to run the schema and then automatically moves to the indicated position
    time.sleep(10)
    pyautogui.moveTo(xWindow, yWindow)
    
    # The process will be okay while the mouse keeps on the indicated positions
    while((pyautogui.position() == (xStop, yStop)) or (pyautogui.position() == (xWindow, yWindow))):
        # Clicking to move the EEG
        pyautogui.moveTo(xWindow, yWindow)
        pyautogui.click()
        time.sleep(timerRefresher/2)
        
        # Clicking to reload the CSV
        pyautogui.moveTo(xStop, yStop)
        pyautogui.click()
        time.sleep(timerRefresher/2)
    
    return

#%% Creating the dataset with the input data and the expected output
def createDataset(xMaximize, yMaximize, xPlay, yPlay, xWindow, yWindow, xStop, yStop, profileName, expectedResult, rangeTime):
    # Check if profile path exists
    if(not(os.path.exists('profiles/' + str(profileName)))):
        os.makedirs('profiles/' + str(profileName))
    time.sleep(0.2)
    
    # Maximizing OpenViBE Designer
    pyautogui.moveTo(xMaximize, yMaximize)
    pyautogui.click()
    time.sleep(1)
    
    # Playing OpenViBE Designer
    pyautogui.moveTo(xPlay, yPlay)
    pyautogui.click()
    time.sleep(rangeTime)
    
    # Clicking over OpenViBE Designer
    pyautogui.moveTo(xWindow, yWindow)
    pyautogui.click()
    time.sleep(0.5)
    
    # Stopping OpenViBE Designer
    pyautogui.moveTo(xStop, yStop)
    pyautogui.click()
    time.sleep(0.5)
    
    # Loading data.csv
    dataframe = pandas.read_csv('data.csv')
    
    # Reworking the dataframe
    dataframe = dataframe.drop(labels='Time:256Hz', axis=1)
    dataframe = dataframe.drop(labels='Epoch', axis=1)
    dataframe = dataframe.drop(labels='Event Id', axis=1)
    dataframe = dataframe.drop(labels='Event Date', axis=1)
    dataframe = dataframe.drop(labels='Event Duration', axis=1)
    
    # Add a column with the expected output
    dataframe.insert(16, "Expected Output", [expectedResult]*len(dataframe))
    
    # Append (or create) the dataset of this selected profile
    if(not(os.path.isfile('profiles/' + str(profileName) + '/dataset.csv'))):
        file = open('profiles/' + str(profileName) + '/dataset.csv', "x")
        file.close()
        dataframe.to_csv('profiles/' + str(profileName) + '/dataset.csv', mode='a', index=False, header=True)
    else:
        dataframe.to_csv('profiles/' + str(profileName) + '/dataset.csv', mode='a', index=False, header=False)
    
    # Remove the data.csv raw file
    os.remove('data.csv')
    
    return

#%% First AI model
def SVM(profileName):
    # Condition if profile or dataset doesn't exists
    if(not(os.path.isfile('profiles/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    return

#%% Second AI model
def b(profileName):
    # Condition if profile or dataset doesn't exists
    if(not(os.path.isfile('profiles/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    return

#%% Third AI model
def c(profileName):
    # Condition if profile or dataset doesn't exists
    if(not(os.path.isfile('profiles/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    return