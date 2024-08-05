from matplotlib import pyplot as plt
import csv
plt.style.use('fivethirtyeight')

roll =[]
pitch = []

# with open('average_path.csv', 'r') as file:
#     reader = csv.reader(file)
#     for i in reader:
#         roll.append(i[0])
#         pitch.append(i[1])

with open('average_path.csv', 'r') as f:
    r = csv.reader(f)
    for ii in r:
        roll.append(float(ii[0]))
        pitch.append(float(ii[1]))

plt.subplot(2, 3, 1)
plt.plot(roll, 'r-')
plt.title('Average Roll')
#plt.ylim(-30, 30)


plt.subplot(2, 3, 2)
plt.plot(pitch, 'g-')
plt.title('Average Pitch')
#plt.ylim(-30, 30)

plt.subplot(2, 3, 4)
plt.plot(pitch, 'b-')
plt.title('Live Pitch')

plt.subplot(2, 3, 5)
plt.plot(pitch, 'y-')
plt.title('Live Pitch')

plt.subplot(1, 3, 3)
plt.bar(range(len(pitch)), pitch)
plt.title('Difference Pitch')

plt.tight_layout()
plt.show()

