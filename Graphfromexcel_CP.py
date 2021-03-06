# Developed by Samson Lamichhane
from typing import List
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from decimal import *
from matplotlib import pyplot as plt
from scipy import integrate
import numpy as np
from array import *

# Developed by Samson Lamichhane


#startPoint=382
startPoint = 394
windowBefore = 100
windowAfter = 300

read_file = pd.read_excel('CP_osc_c.xlsx')
df = pd.read_excel('CP_osc_c.xlsx')
df4 = pd.read_excel('CP_osc_c.xlsx')
df5 = pd.read_excel('CP_osc_c.xlsx')

df["Time (ms)"] = pd.to_numeric(df["Time (ms)"], downcast="float")
df["x-axis acceleration"] = pd.to_numeric(df["x-axis acceleration"], downcast="float")
df["x-axis acceleration"] = ((df["x-axis acceleration"] * 9.81) / 8192)

df["y-axis acceleration"] = pd.to_numeric(df["y-axis acceleration"], downcast="float")
df["y-axis acceleration"] = ((df["y-axis acceleration"] * 9.81) / 8192)

df["z-axis acceleration"] = pd.to_numeric(df["z-axis acceleration"], downcast="float")
df["z-axis acceleration"] = ((df["z-axis acceleration"] * 9.81) / 8192)


xGyroOffset = -0.088976965;
yGyroOffset = -0.753604336;
zGyroOffset = -1.248733062;



df["x-axis gyroscope"] = pd.to_numeric(df["x-axis gyroscope"], downcast="float")
df["x-axis gyroscope"] = (df["x-axis gyroscope"] / 16.4) - xGyroOffset

df["y-axis gyroscope"] = pd.to_numeric(df["y-axis gyroscope"], downcast="float")
df["y-axis gyroscope"] = (df["y-axis gyroscope"] / 16.4) - yGyroOffset

df["z-axis gyroscope"] = pd.to_numeric(df["z-axis gyroscope"], downcast="float")
df["z-axis gyroscope"] = (df["z-axis gyroscope"] / 16.4) - zGyroOffset

df["x-axis magnetometer"] = pd.to_numeric(df["x-axis magnetometer"], downcast="float")
df["x-axis magnetometer"] = (df["x-axis magnetometer"] * 0.6)

df["y-axis magnetometer"] = pd.to_numeric(df["y-axis magnetometer"], downcast="float")
df["y-axis magnetometer"] = (df["y-axis magnetometer"] * 0.6)

df["z-axis magnetometer"] = pd.to_numeric(df["z-axis magnetometer"], downcast="float")
df["z-axis magnetometer"] = (df["z-axis magnetometer"] * 0.6)
df5 = df
df = df[startPoint - windowBefore-1 : startPoint + windowAfter]

t_trimmed = np.arange(0, 4010, 10)

gx_int = integrate.cumtrapz(df['x-axis gyroscope'], dx=0.01)
gy_int = integrate.cumtrapz(df['y-axis gyroscope'], dx=0.01)
gz_int = integrate.cumtrapz(df['z-axis gyroscope'], dx=0.01)

gx_int = pd.Series(gx_int)
#gy_int = pd.Series(gy_int)
gz_int = pd.Series(gz_int)

ax = plt.gca()

gx_trimmed = df['x-axis gyroscope'].tolist()
gy_trimmed = df['y-axis gyroscope'].tolist()
gz_trimmed = df['z-axis gyroscope'].tolist()

t_trimmed = t_trimmed.tolist()
gx_int = gx_int.tolist()
gy_int = gy_int.tolist()
gz_int = gz_int.tolist()

gx_int1 = gx_int
gy_int1 = gy_int
gz_int1 = gz_int

gx_int.insert(0,0)
gy_int.insert(0,0)
gz_int.insert(0,0)

plt.title('Y-axis gyroscope')
plt.xlabel('time(ms)')
plt.ylabel('°')
plt.plot(t_trimmed, gy_trimmed,label='Angular Velocity')
plt.plot(t_trimmed, gy_int, label='Angular Displacement')
plt.legend()
plt.show()

ay = plt.gca()

plt.title('Accelerometer Data')
df.plot(kind='line', x='Time (ms)', y='x-axis acceleration', ax=ay)
df.plot(kind='line', x='Time (ms)', y='y-axis acceleration', ax=ay, color='red')
df.plot(kind='line', x='Time (ms)', y='z-axis acceleration', ax=ay, color='black')
plt.xlabel('time(ms)')
plt.ylabel('Acceleration (m/s^2)')
plt.show()

az = plt.gca()

plt.title('Gyroscope  Data')
df.plot(kind='line', x='Time (ms)', y='x-axis gyroscope', ax=az)
df.plot(kind='line', x='Time (ms)', y='y-axis gyroscope', ax=az, color='red')
df.plot(kind='line', x='Time (ms)', y='z-axis gyroscope', ax=az, color='black')
plt.xlabel('time(ms)')
plt.ylabel('Angular Velocity °/s')
plt.show()

a1 = plt.gca()

plt.title('Magnetometer  Data')
df.plot(kind='line', x='Time (ms)', y='x-axis magnetometer', ax=a1)
df.plot(kind='line', x='Time (ms)', y='y-axis magnetometer', ax=a1, color='red')
df.plot(kind='line', x='Time (ms)', y='z-axis magnetometer', ax=a1, color='black')
plt.xlabel('time(ms)')
plt.ylabel('Magnetic Field Strength')
plt.show()

a2 = plt.gca()

plt.title('Choosing the start point in the graph')
df5.plot(kind='line', x='Time (ms)', y='x-axis acceleration', ax=a2)
df5.plot(kind='line', x='Time (ms)', y='y-axis acceleration', ax=a2, color='red')
df5.plot(kind='line', x='Time (ms)', y='z-axis acceleration', ax=a2, color='black')
df5.plot(kind='line', x='Time (ms)', y='x-axis gyroscope', ax=a2, color='green')
df5.plot(kind='line', x='Time (ms)', y='y-axis gyroscope', ax=a2, color='yellow')
df5.plot(kind='line', x='Time (ms)', y='z-axis gyroscope', ax=a2, color='blue')
plt.show()

read_file1 = pd.read_excel('CP_toenter.xlsx')
df1 = pd.read_excel('CP_toenter.xlsx')
df2 = pd.read_excel('CP_osc.xlsx')
df['total_gyro_vector'] = df['x-axis gyroscope'] + df['y-axis gyroscope'] + df['z-axis gyroscope']


t1 = [a * b for a, b in zip(gx_int, gx_int)]
t2 = [a * b for a, b in zip(gy_int, gy_int)]
t3 = [a * b for a, b in zip(gz_int, gz_int)]

total = []

for i in range(0, len(t1)):
    total.append(t1[i] + t2[i]+t3[i])

total = np.array(total)
total_angle_vector = np.sqrt(total)
total_angle_vector = total_angle_vector.tolist()


total_gyro_vector = df['total_gyro_vector'].tolist()

a3 = plt.gca()
plt.title('CP Gyroscope Measurement')
plt.plot(t_trimmed, total_gyro_vector, label= 'Angular Velocity')
plt.plot(t_trimmed, total_angle_vector, label='Angular Displacement')
plt.xlabel('Time(ms)')
plt.ylabel('Angle °')
plt.legend()
plt.show()

gy_int = pd.DataFrame(gy_int)

DatabasePoint = 104
ID9_meas = (gy_int * -1) + 135
total_angle_vector = pd.DataFrame(total_angle_vector)
ID9_meas_total = (total_angle_vector * -1) + 135

df2 = df2[DatabasePoint-1:]
df2['ID9_meas']=ID9_meas #when Trimmed


ID9_meas_trimmed = df2['ID9_meas'].tolist()
df2['ID9_meas_total'] = ID9_meas_total
ID9_meas_total = df2['ID9_meas_total'].tolist()

ID9_meas_trimmed = [ID9_meas_trimmed for ID9_meas_trimmed in ID9_meas_trimmed if str(ID9_meas_trimmed) != 'nan']
ID9_meas_trimmed_total = [ID9_meas_total for ID9_meas_total in ID9_meas_total if str(ID9_meas_total) != 'nan']

t_trimmed_trimmed = np.arange(0,2980,10)
t_trimmed_trimmed = t_trimmed_trimmed.tolist()


a4 = plt.gca()
plt.title('Servo ID9 Angle')
plt.plot(t_trimmed_trimmed,ID9_meas_trimmed,label='Measured ID9 angle from y-axis')
plt.plot(t_trimmed_trimmed,ID9_meas_trimmed_total, label='measured ID9 angle from total gyro vector')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=a4, color='blue')
plt.xlabel('Time(ms)')
plt.ylabel('ID9 servo angle')
plt.legend()
plt.show()

a5 = plt.gca()
plt.title('CP Servo ID9 Angle')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=a5, color='blue')
plt.plot(t_trimmed_trimmed, ID9_meas_trimmed_total, label='Measured Angle')
plt.xlabel('Time(ms)')
plt.ylabel('Angle')
plt.legend()
plt.show()


a6 = plt.gca()
plt.title('CP 3-axis Angular Displacement and Vector Sum')

plt.plot(t_trimmed, gx_int1, label='x-axis')
plt.plot(t_trimmed, gy_int1, label='y-axis')
plt.plot(t_trimmed, gz_int1, label='z-axis')
plt.plot(t_trimmed,total_angle_vector,label='Vector')
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')

plt.legend()

plt.show()

a7 = plt.gca()
plt.title('CP Gyroscope Raw Data')
plt.plot(t_trimmed,gx_trimmed,label='x-axis')
plt.plot(t_trimmed,gy_trimmed,label='y-axis')
plt.plot(t_trimmed,gz_trimmed,label='z-axis')
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.legend()
plt.show()


ID9_entered_angle_1192element = np.arange(842)

ID9_entered_angle_1192element[1] = 135


i = 2
ID9_entered_angle_1192element=ID9_entered_angle_1192element.astype('float64')
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] - 55 / 105
    i=i+1
    if i == 105:
        break
ID9_entered_angle_1192element[105]=80.5238
ID9_entered_angle_1192element[106] = 80
i = 107
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] + 39 / 105
    i = i + 1
    if i == 210:
        break
ID9_entered_angle_1192element[210] = 1.186285714285709e+02
ID9_entered_angle_1192element[211] = 119
i = 212
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] - 41 / 105
    i = i + 1
    if i == 315:
        break
ID9_entered_angle_1192element[315] = 78.3904761904760
ID9_entered_angle_1192element[316] = 78
i = 317
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] + 25 / 105
    i = i + 1
    if i == 420:
        break
ID9_entered_angle_1192element[420] = 1.027619047619050e+02
ID9_entered_angle_1192element[421] = 103

i = 422
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] - 28 / 105
    i = i + 1
    if i == 525:
        break
ID9_entered_angle_1192element[525] = 75.266666666666770
ID9_entered_angle_1192element[526] = 75


i = 527
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] + 11 / 105
    i = i + 1
    if i == 630:
        break

ID9_entered_angle_1192element[630] = 85.8952380952377
ID9_entered_angle_1192element[631] = 86


i = 632
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] -13 / 105
    i = i + 1
    if i == 735:
        break
ID9_entered_angle_1192element[735] = 73.123809523809200
ID9_entered_angle_1192element[736] = 73
i = 737
while ID9_entered_angle_1192element[i] < ID9_entered_angle_1192element.size:
    ID9_entered_angle_1192element[i] = ID9_entered_angle_1192element[i - 1] -3/ 105
    i = i + 1
    if i == 840:
        break
ID9_entered_angle_1192element[840] = 70.028571428571810
ID9_entered_angle_1192element[841] = 70

End_70s_a = 70*np.ones(351)
End_70s_a = End_70s_a.tolist()


ID9_entered_angle_1192element1 = ID9_entered_angle_1192element

ID9_entered_angle_1192element = ID9_entered_angle_1192element.tolist()
ID9_entered_angle_1192element.pop(0)

ID9_entered_angle_1192element_final = ID9_entered_angle_1192element + End_70s_a

ID9_entered_angle_1192element_final1 = np.array(ID9_entered_angle_1192element_final)



ID9_entered_angle_298element = np.arange(299)
ID9_entered_angle_298element=ID9_entered_angle_298element.astype(float)
ID9_entered_angle_298element[0] = 135
ID9_entered_angle_298element[1] =135
i = 2
while i <= 298:

    ID9_entered_angle_298element[i] = ID9_entered_angle_1192element_final1[1+4*(i-1)]
    i = i + 1


ID9_entered_angle_298element = ID9_entered_angle_298element.tolist()
ID9_entered_angle_298element.pop(0)



time_2970_1192entries=np.arange(1192)
time_2970_1192entries=time_2970_1192entries.astype(float)

time_2970_1192entries[1] = 0


i = 1
while i <= 1191:

    time_2970_1192entries[i] = time_2970_1192entries[i-1] + 2.5
    i = i + 1

time_2970_1192entries = time_2970_1192entries.tolist()


a8 = plt.gca()
plt.title('Test Plot')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=a8, color='brown')
plt.plot(time_2970_1192entries,ID9_entered_angle_1192element_final)
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()


a9 = plt.gca()
plt.title('Test Plot 2')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=a9, color='brown')
plt.plot(t_trimmed_trimmed,ID9_entered_angle_298element)
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()

R = np.corrcoef(ID9_entered_angle_298element, ID9_meas_trimmed_total)
from sklearn.metrics import mean_squared_error
from math import sqrt

Rms = sqrt(mean_squared_error(ID9_entered_angle_298element, ID9_meas_trimmed_total))
