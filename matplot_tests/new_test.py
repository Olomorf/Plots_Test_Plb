import csv
import random
import time

import matplotlib
from matplotlib import pyplot as plt
from drawnow import drawnow
from datetime import datetime

#---------------------- CONSTANTS & GLOBALS
SIZE_OF_LAP = 5  # sec
SET_AVERAGE_PATH = False
TOTAL_NUMBER_LAPS = 5  # Total number of records for the avg path

current_number_laps = 1
avg_roll = []
avg_pitch = []
roll = []
pitch = []

#---------------------- FUNCTIONS

#---------------------- INITIALIZATION

plt.style.use('fivethirtyeight')
plt.ion()


def save_to_csv():
    with open('average_path.csv', 'w') as file:
        writer = csv.writer(file) # clear the file
    with open('average_path.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        for r, p in zip(roll, pitch):
            writer.writerow((r, p))
            print(f'{r} - {p}')
def make_average():
    global avg_roll, avg_pitch
    try:
        with open('average_path.csv', 'r') as f:
            r = csv.reader(f)
            for indx in r:
                avg_roll.append(float(indx[0]))
                avg_pitch.append(float(indx[1]))
        print(f'AVG ROLL = {avg_roll}')
        print(f'AVG PITCH = {avg_pitch}')
        # new_pitch = [(float(a) + float(b)) / 2 for a, b in zip(avg_pitch, pitch)]
        # new_roll = [(float(a) + float(b)) / 2 for a, b in zip(avg_roll, roll)]
        new_pitch = []
        new_roll = []
        for nums in range(len(pitch)):
            new_pitch.append((float(avg_pitch[nums]) + float(pitch[nums]))/2)
            new_roll.append((float(avg_roll[nums]) + float(roll[nums])) / 2)
        print(f'New pitch = {new_pitch}')
        print(f'New roll = {new_roll}')

        # save the values in a new file
        with open('average_path.csv', 'w') as fls:
            writer = csv.writer(fls)
        with open('average_path.csv', 'a', newline="") as write:
            writer = csv.writer(write)
            for r, p in zip(new_roll, new_pitch):
                writer.writerow((r, p))

        avg_roll = new_roll
        avg_pitch = new_pitch

    except FileNotFoundError:
        save_to_csv()

def plot():

    plt.clf()
    #pltax2.cla()

    plt.subplot(2, 3, 1)
    plt.plot(avg_roll, 'r-')
    plt.title('Average Roll')
    plt.ylim(-30, 30)

    plt.subplot(2, 3, 2)
    plt.plot(avg_pitch, 'g-')
    plt.title('Average Pitch')
    plt.ylim(-30, 30)

    # Plot Live Roll
    plt.subplot(2, 3, 4)
    plt.plot(roll, 'b-')
    plt.title('Live Roll')
    plt.ylim(-30, 30)

    # Plot Live Pitch
    plt.subplot(2, 3, 5)
    plt.plot(pitch, 'm-')
    plt.title('Live Pitch')
    plt.ylim(-30, 30)



    #Compare and scatter differences
    if avg_roll and avg_pitch:
        # diff_roll = [r - a for r, a in zip(roll, avg_roll)]
        # diff_pitch = [p - a for p, a in zip(pitch, avg_pitch)]
        diff_roll = []
        diff_roll_index = []
        diff_pitch = []
        diff_pitch_index = []
        for counter in range(len(roll)):
            number = avg_roll[counter] - roll[counter]
            number2 = avg_pitch[counter] - pitch[counter]
            if number > 1 or number < 1:
                if number < 0:
                    number = number * -1
                diff_roll.append(number)
                diff_roll_index.append(counter)
            if number2 > 1 or number2 < 1:
                if number2 < 0:
                    number2 = number2 * -1
                diff_pitch.append(number2)
                diff_pitch_index.append(counter)

        plt.subplot(1, 3, 3)
        plt.bar(diff_roll_index, diff_roll)
        plt.ylim(-30, 30)
        plt.subplot(1, 3, 3)
        plt.bar(diff_pitch_index, diff_pitch)
        plt.ylim(-30, 30)

    plt.tight_layout()


def save_figure():
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    plt.savefig(f'plot_{timestamp}.png')



# Plotting Static Data (Average Path)

try:
    with open('average_path.csv', 'r') as f:
        r = csv.reader(f)
        for indx in r:
            avg_roll.append(float(indx[0]))
            avg_pitch.append(float(indx[1]))

except FileNotFoundError:
    print("Average path file not found. Initializing with empty values.")

#---------------------- MAIN LOOP
i = 0
while True:
    # if i == SIZE_OF_LAP:  # Save the figure every 10 iterations as an example
    #     #save_figure()
    #      break
    # Simulate getting data
    with open('output_data.csv', 'r') as file:
        reader = csv.reader(file)
        for _ in reader:
            roll.append(float(_[0]))
            pitch.append(float(_[1]))
    print(f'I = {i}')
    print(f'Current laps = {current_number_laps}')
    if SET_AVERAGE_PATH:
        if current_number_laps <= TOTAL_NUMBER_LAPS:
            if i == (SIZE_OF_LAP - 1):
                make_average()
                roll.clear()
                pitch.clear()
                i = -1
                current_number_laps += 1
        else:
            SET_AVERAGE_PATH = False
            i = 0
            continue

    drawnow(plot)
    plt.pause(0.00001)

    i += 1
    # if i == SIZE_OF_LAP:
    #     save_figure()
    #     break
    time.sleep(1)
