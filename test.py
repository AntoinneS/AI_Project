import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 12
patients = (90, 55, 40, 65, 0, 0 , 0 ,0 ,0, 0, 0 ,0)
riskpatients = (85, 62, 54, 20, 0, 0, 0, 0, 0, 0,0 ,0)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, patients, bar_width,
alpha=opacity,
color='b',
label='Patients')

rects2 = plt.bar(index + bar_width, riskpatients, bar_width,
alpha=opacity,
color='r',
label='Patients at Risk')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
plt.legend()

plt.tight_layout()
plt.show()