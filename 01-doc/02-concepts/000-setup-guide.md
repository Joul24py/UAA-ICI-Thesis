# Setting up Emotiv Epoc+ with computer

As this project is based in the Emotiv headsets, it's necessary to download the appropiate software from the [Emotiv downloads](https://www.emotiv.com/emotiv-launcher/) official page, downloading the Emotiv Launcher as a first step.

![](/01-doc/02-concepts/img/1.png)

It's also neccesary to [register for an Emotiv ID](https://www.emotiv.com/my-account/).

![](/01-doc/02-concepts/img/2.png)

In a personal experience, I decided to install the entire offered software in the installation:

- Emotiv Launcher
- Emotiv BrainViz
- EmotivPRO
- EmotivBCI

![](/01-doc/02-concepts/img/3.png)

After this, you should run the Emotiv Launcher with the neuroheadset correctly paired and connected via USB. It should appear as a possible connection when it's running the Emotiv Launcher.

![](/01-doc/02-concepts/img/4.png)

Then it has to be correctly placed in order to detect efficiently the neural activity. Once it's done this, the Emotiv Setup is over, so now it's time to use the [CymatiCorp repository: Cykit](https://github.com/CymatiCorp/CyKit).

# Downloading Cykit

The Cykit download can be found in the [Cykit installation guide](https://github.com/CymatiCorp/CyKit/wiki/How-to-Install-CyKIT).

## Setting up Cykit and first data recovery

As well as a basic setup can be found in the [Cykit stream data guide using OpenViBE](https://github.com/CymatiCorp/CyKit/wiki/How-to-Stream-Data-to-OpenViBE). The following instructions will take from the last step of the previous guide when all the OpenViBE configurations are done.

# Simulating a live analysis

Once the first setup is done, it's necessary to make some changes to the suggested configurations by CymatiCorp.

As this personal project needs the data recovered by the headset, it is necessary to get the data in any way. To do so, it should be added in the OpenViBE designer schema another element which can be found in the ```"File reading and writing"```. Inside of it, go to the ```"CSV"``` folder and drag and drop the ```"CSV File Writer"``` element into the schema.

![](/01-doc/02-concepts/img/5.png)

It's necessary to connect the pink output arrow from the ```"Acquisition Client"``` to the pink input arrow from the new element.

![](/01-doc/02-concepts/img/6.png)

It's also necessary to customize some elements when double click over the CSV File Writer element:

![](/01-doc/02-concepts/img/7.png)

In the ```"Filename"``` field it will be the directory where the CSV file is going to be stored (it can be choose as a preference of the user and not necessary the same as this tutorial).

It's also necessary to mark as ```true``` in the ```"Append Data"``` field. Then click on ```"Apply"``` and save the schema.

Then, before to start the scenario, it's necessary to mark the ```"run the scenario in a loop"``` button because the software would create a CSV until the end of the experiment and personally I couldn't find an element that let me to the analysis live while the data recollection is in progress.

![](/01-doc/02-concepts/img/8.png)

This is not the only configuration that is needed to stream live the data while reading it from the headset. It's also needed to use the PyAutoGUI library from Python.

## The PyAutoGUI library

The PyAutoGUI library lets your Python scripts control the mouse and keyboard to automate interactions with other applications. All the documentation of this library can be found in the [PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/).

First of all it's necessary to install the library with the Python ```pip``` tool using the following command:

```bash
pip install pyautogui
```

After this, we will use this library to create a script in order to stop automatically and periodically the process that the OpenViBE designer does of reading data (because when the stop process is executed is when the CSV file is generated).

First of all it's necessary to locate the coordinates where the button is in our screen. For that is used the following script (which can be found also in this repository as the [00-mouse-position.py](https://github.com/Joul24py/UAA-ICI-Thesis/blob/main/02-code/02-code/00-mouse-position.py) file):

```python
import pyautogui
import time

# Sleeping the script so we have time to set the mouse on its position
time.sleep(10)

# Getting the mouse position
print(pyautogui.position())
```

Then, when we have this values, we can store them in ```x``` and ```y``` variables that we'll use in the following script. Now, when everything is ready to be executed, the headset connected, Emotiv running, OpenViBE fully connected and configured, it's time to run the following script (which can be found also in this repository as the [01-run-update-stream.py](https://github.com/Joul24py/UAA-ICI-Thesis/blob/main/02-code/02-code/01-run-update-stream.py) file):

```python
import pyautogui
import time

x = 0
y = 0

# Sleeping the script so we have time to run the schema and then automatically moves to the indicated position
time.sleep(10)
pyautogui.moveTo(x, y)

# The process will be okay while the mouse keeps on the indicated position 
while(pyautogui.position() == (x, y)):
   pyautogui.click()
   time.sleep(1) # The CSV is getting updated each second
```
