"""
Todo
- make a script that generates entries of roll & pitch values in a file
- make a function that averages N times the roll & pitch values for each index
- plot the average and the new generated live data in 2 subplots, each subplot having 2subplots as well
- compare those values and where its a difference add a scatter point
- save if possible the resulted figure with the name d-m-y_H-M
"""
import csv
import random
import time
from matplotlib import pyplot as plt
from drawnow import *

# import pandas as pd


#----------------------     CONSTANTS & GLOBALS
SIZE_OF_LAP = 5 #sec
SET_AVERAGE_PATH = False
TOTAL_NUMBER_LAPS = 5 # total number of records for the avg path


current_number_laps = 1

avg_roll = []
avg_pitch = []
roll = []
pitch = []
#----------------------

plt.style.use('fivethirtyeight')
plt.ion()
fig, ax = plt.subplots(2, 2)


#----------------------     FUNCTIONS

def save_to_csv():
    with open('average_path.csv', 'w') as file:
        writer = csv.writer(file) # clear the file
    with open('average_path.csv', 'a', newline="") as f:
        w = csv.writer(f)
        for _ in range(len(roll)):
            data = (roll[_], pitch[_])
            print(data)
            w.writerow(data)

def make_average():
    """
    takes the data from the original_path file and puts it in the 2 lists
    if original path not generated then creates it with the current data.
    After the avg_roll, avg_pitch are initialized, takes the current generated data
    and makes an avg, result is stored in original_path file.
    :return: None
    """
    try:
        with open('average_path.csv', 'r') as f:
            r = csv.reader(f)
            for ii in r:
                avg_roll.append(ii[0])
                avg_pitch.append(ii[1])
        new_pitch =[]
        new_roll = []
        for val1, val2 in zip(avg_pitch, pitch):
            new_pitch.append((float(val1)+float(val2))/2)
        for val3, val4 in zip(avg_roll, roll):
            new_roll.append((float(val3)+float(val4))/2)

        #save the values in a new file
        with open('average_path.csv', 'w') as fls:
            writer = csv.writer(fls)

        with open('average_path.csv', 'a', newline="") as write:
             wrt = csv.writer(write)
             for datas in range(len(new_pitch)):
                 obj = (new_roll[datas], new_pitch[datas])
                 wrt.writerow(obj)
        new_pitch.clear()
        new_roll.clear()

    except FileNotFoundError:
        with open('average_path.csv', 'a', newline="") as fff:
            www = csv.writer(fff)
            for __ in range(len(roll)):
                new_data = (roll[__], pitch[__])
                www.writerow(new_data)



def plot():
    # with open('average_path.csv', 'r') as f:
    #     r = csv.reader(f)
    #     for ii in r:
    #         avg_roll.append(ii[0])
    #         avg_pitch.append(ii[1])


    ax[1, 0].cla()  # Clear the current figure
    ax[1, 1].cla()
    # Plot Live Roll
    ax[1, 0].plot(roll, 'b-')
    ax[1, 0].set_title('Live Roll')
    ax[1, 0].set_ylim(-30, 30)

    # Plot Live Pitch
    ax[1, 1].plot(pitch, 'm-')
    ax[1, 1].set_title('Live Pitch')
    ax[1, 1].set_ylim(-30, 30)
    plt.tight_layout()  # Adjust layout to prevent overlap


if not SET_AVERAGE_PATH:
    with open('average_path.csv', 'r') as f:
        r = csv.reader(f)
        for ii in r:
            avg_roll.append(ii[0])
            avg_pitch.append(ii[1])

    ax[0, 0].plot(avg_roll, 'r-')
    ax[0, 0].set_title('Average Roll')
    ax[0, 0].set_ylim(-30, 30)
    # Plot Average Pitch

    ax[0, 1].plot(avg_pitch, 'g-')
    ax[0, 1].set_title('Average Pitch')
    ax[0, 1].set_ylim(-30, 30)
    plt.show()

#----------------------
i = 0
while True:
    #gets the data
    with open('output_data.csv', 'r') as file:
        reader = csv.reader(file)
        for _ in reader:
            roll.append(float(_[0]))
            pitch.append(float(_[1]))
    #sets the average path

    if SET_AVERAGE_PATH: #if make new average path
        print(f'I = {i}')
        print(f'Number of laps = {current_number_laps}')
        if current_number_laps != TOTAL_NUMBER_LAPS:
            #make avg
            if i == (SIZE_OF_LAP-1):
                make_average()
                roll.clear()
                pitch.clear()
                i = -1
                current_number_laps = current_number_laps + 1
        else:
            SET_AVERAGE_PATH = False
            i = 0
            continue
    # else:
    #     print(SET_AVERAGE_PATH)
    #     break
    drawnow(plot)
    plt.pause(.0001)


    i = i + 1
    time.sleep(1)

