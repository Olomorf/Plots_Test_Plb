import csv
import random
import time

# fieldnames = ['roll', 'pitch']

while True:
    # with open('output_data.csv', 'w') as file:
    #     csv_writer = csv.writer(file)

    with open('output_data.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        # data = {
        # "roll": random.randint(-45, 45),
        # "pitch": random.randint(-45, 45)
        # }
        data = (random.randint(-30, 30), random.randint(-30, 30))
        print(data)
        writer.writerow(data)
    time.sleep(1)