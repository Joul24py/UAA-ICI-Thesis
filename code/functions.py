#%% Libraries
import os
import time
import random
import pyautogui
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from scipy.stats import zscore
import sklearn.exceptions
import warnings

warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)

#%% Whole profile
AllProfiles = ['joul1',
'pep1',
'mom1',
'dad1',
'Roman1',
'Hiram1',
'Meli1',
'Oscar1',
'Bere1',
'Andy1',
'Montse1',
'Abraham1',
'Valeria1',
'Juliett1',
'Gus1',
'Alex1',
'Meza1',
'Fer1',
'Eloy1',
'Jorge2do1',
'Diego2do1',
'Raul2do1',
'Padilla1',
'Yissel1',
'Daniela1',
'Isabela1',
'Yolanda1',
'joul2',
'pep2',
'mom2',
'dad2',
'Roman2',
'Hiram2',
'Meli2',
'Oscar2',
'Bere2',
'Andy2',
'Montse2',
'Abraham2',
'Valeria2',
'Juliett2',
'Gus2',
'Alex2',
'Meza2',
'Fer2',
'Eloy2',
'Jorge2do2',
'Diego2do2',
'Raul2do2',
'Padilla2',
'Yissel2',
'Daniela2',
'Isabela2',
'Yolanda2']

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
    dataframe.insert(14, "Expected Output", [expectedResult]*len(dataframe))
    
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
    if(not(os.path.isfile('normz/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    
    # Support Vector Machine process
    df = pandas.read_csv('normz/' + str(profileName) + '/dataset.csv')
    
    X = df.drop(['Expected Output'], axis = 1)
    Y = df['Expected Output']
    
    xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.20)
    
    classifier = SVC(kernel = 'linear')
    classifier.fit(xtrain, ytrain)
    
    ypred = classifier.predict(xtest)
    print(ypred)
    
    print(classification_report(ytest, ypred))
    
    matriz = confusion_matrix(ytest, ypred)
    print('Matriz de Confusión')
    print(matriz)

    precision = precision_score(ytest, ypred, pos_label="a", average=None)
    print('Precisión del modelo')
    print(precision)
    
    return precision

#%% Second AI model
def NaiveBayes(profileName):
    # Condition if profile or dataset doesn't exists
    if(not(os.path.isfile('normz/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    
    # Naive Bayes process
    df = pandas.read_csv('normz/' + str(profileName) + '/dataset.csv')

    X = df.drop(['Expected Output'], axis = 1)
    Y = df['Expected Output']

    xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.20)

    classifier = GaussianNB()
    classifier.fit(xtrain, ytrain)

    ypred = classifier.predict(xtest)

    matriz = confusion_matrix(ytest, ypred)
    print('Matriz de Confusión')
    print(matriz)

    precision = precision_score(ytest, ypred, pos_label="a", average=None)
    print('Precisión del modelo')
    print(precision)
    
    return precision

#%% Third AI model
def RandomForest(profileName):
    # Condition if profile or dataset doesn't exists
    if(not(os.path.isfile('normz/' + str(profileName) + '/dataset.csv'))):
        print('User not found or dataset not created yet')
        return
    
    # Random Forest process
    df = pandas.read_csv('normz/' + str(profileName) + '/dataset.csv')

    X = df.drop(['Expected Output'], axis = 1)
    Y = df['Expected Output']

    xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size = 0.20)

    sc = StandardScaler()
    xtrain = sc.fit_transform(xtrain)
    xtest = sc.fit_transform(xtest)

    classifier = RandomForestClassifier(n_estimators = 4)
    classifier.fit(xtrain, ytrain)

    ypred = classifier.predict(xtest)

    matriz = confusion_matrix(ytest, ypred)
    print('Matriz de Confusión')
    print(matriz)

    precision = precision_score(ytest, ypred, pos_label="a", average=None)
    print('Precisión del modelo')
    print(precision)
    
    return precision

#%% Getting every precision value
def runModels(users):
    resultsFile = open("results.txt", 'w')
    resultsFile.write("SVM\n\n")
    print("SVM")
    
    for i in users:
        resultsFile.write(i + "\n")
        print("Usuario: " + i)
        for j in range(5):
            print("Iteración: " + str(j + 1))
            result = SVM(i)
            resultsFile.write(str(result) + "\n")
        resultsFile.write("\n")
    
    resultsFile.write("Naive Bayes\n\n")
    print("Naive Bayes")
    
    for i in users:
        resultsFile.write(i + "\n")
        print("Usuario: " + i)
        for j in range(5):
            print("Iteración: " + str(j + 1))
            result = NaiveBayes(i)
            resultsFile.write(str(result) + "\n")
        resultsFile.write("\n")
    
    resultsFile.write("Random Forest\n\n")
    print("Random Forest")
    
    for i in users:
        resultsFile.write(i + "\n")
        print("Usuario: " + i)
        for j in range(5):
            print("Iteración: " + str(j + 1))
            result = RandomForest(i)
            resultsFile.write(str(result) + "\n")
        resultsFile.write("\n")
    
    resultsFile.close()
    return

#%% Z-Normalization
def NormZ(profileName):
    for i in profileName:
        # Condition if profile or dataset doesn't exists
        if(not(os.path.isfile('normz/' + str(i) + '/dataset.csv'))):
            print('User not found or dataset not created yet')
            return
        
        # Z-Normalization
        df = pandas.read_csv('normz/' + str(i) + '/dataset.csv')
        
        df['Channel 1'] = zscore(df['Channel 1'])
        df['Channel 2'] = zscore(df['Channel 2'])
        df['Channel 3'] = zscore(df['Channel 3'])
        df['Channel 4'] = zscore(df['Channel 4'])
        df['Channel 5'] = zscore(df['Channel 5'])
        df['Channel 6'] = zscore(df['Channel 6'])
        df['Channel 7'] = zscore(df['Channel 7'])
        df['Channel 8'] = zscore(df['Channel 8'])
        df['Channel 9'] = zscore(df['Channel 9'])
        df['Channel 10'] = zscore(df['Channel 10'])
        df['Channel 11'] = zscore(df['Channel 11'])
        df['Channel 12'] = zscore(df['Channel 12'])
        df['Channel 13'] = zscore(df['Channel 13'])
        df['Channel 14'] = zscore(df['Channel 14'])
        
        df.to_csv('normz/' + str(i) + '/dataset.csv', index = False)
    
    return

#%% Fourier Transformation
def Fourier(profileName):
    for i in profileName:
        # Condition if profile or dataset doesn't exists
        if(not(os.path.isfile('fourier/' + str(i) + '/dataset.csv'))):
            print('User not found or dataset not created yet')
            return
        
        # Z-Normalization
        df = pandas.read_csv('fourier/' + str(i) + '/dataset.csv')
        
        channel1 = np.array(df['Channel 1'])
        channel2 = np.array(df['Channel 2'])
        channel3 = np.array(df['Channel 3'])
        channel4 = np.array(df['Channel 4'])
        channel5 = np.array(df['Channel 5'])
        channel6 = np.array(df['Channel 6'])
        channel7 = np.array(df['Channel 7'])
        channel8 = np.array(df['Channel 8'])
        channel9 = np.array(df['Channel 9'])
        channel10 = np.array(df['Channel 10'])
        channel11 = np.array(df['Channel 11'])
        channel12 = np.array(df['Channel 12'])
        channel13 = np.array(df['Channel 13'])
        channel14 = np.array(df['Channel 14'])
        
        transform1 = np.fft.fft(channel1)
        transform2 = np.fft.fft(channel2)
        transform3 = np.fft.fft(channel3)
        transform4 = np.fft.fft(channel4)
        transform5 = np.fft.fft(channel5)
        transform6 = np.fft.fft(channel6)
        transform7 = np.fft.fft(channel7)
        transform8 = np.fft.fft(channel8)
        transform9 = np.fft.fft(channel9)
        transform10 = np.fft.fft(channel10)
        transform11 = np.fft.fft(channel11)
        transform12 = np.fft.fft(channel12)
        transform13 = np.fft.fft(channel13)
        transform14 = np.fft.fft(channel14)
        
        df['Channel 1'] = transform1
        df['Channel 2'] = transform2
        df['Channel 3'] = transform3
        df['Channel 4'] = transform4
        df['Channel 5'] = transform5
        df['Channel 6'] = transform6
        df['Channel 7'] = transform7
        df['Channel 8'] = transform8
        df['Channel 9'] = transform9
        df['Channel 10'] = transform10
        df['Channel 11'] = transform11
        df['Channel 12'] = transform12
        df['Channel 13'] = transform13
        df['Channel 14'] = transform14
        
        df.to_csv('fourier/' + str(i) + '/dataset.csv', index = False)
    
    return