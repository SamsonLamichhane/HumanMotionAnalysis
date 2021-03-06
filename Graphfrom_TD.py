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

startPoint = 293
windowBefore = 100
windowAfter = 650

read_file = pd.read_excel('TD_osc_c_1.xlsx')
df = pd.read_excel('TD_osc_c_1.xlsx')
df5 = pd.read_excel('TD_osc_c_1.xlsx')
df4 = pd.read_excel('TD_osc_c_1.xlsx')

df["Time (ms)"] = pd.to_numeric(df["Time (ms)"], downcast="float")
df["x-axis acceleration"] = pd.to_numeric(df["x-axis acceleration"], downcast="float")
df["x-axis acceleration"] = ((df["x-axis acceleration"] * 9.81) / 8192)

df["y-axis acceleration"] = pd.to_numeric(df["y-axis acceleration"], downcast="float")
df["y-axis acceleration"] = ((df["y-axis acceleration"] * 9.81) / 8192)

df["z-axis acceleration"] = pd.to_numeric(df["z-axis acceleration"], downcast="float")
df["z-axis acceleration"] = ((df["z-axis acceleration"] * 9.81) / 8192)

xGyroOffset = -0.088976965
yGyroOffset = -0.753604336
zGyroOffset = -1.248733062


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

df = df[startPoint - windowBefore-1:startPoint + windowAfter]

gx_int = integrate.cumtrapz(df['x-axis gyroscope'], dx=0.01)
gy_int = integrate.cumtrapz(df['y-axis gyroscope'], dx=0.01)
gz_int = integrate.cumtrapz(df['z-axis gyroscope'], dx=0.01)

gx_int = gx_int.tolist()
gy_int = gy_int.tolist()
gz_int = gz_int.tolist()

gx_int.insert(0,0)
gy_int.insert(0,0)
gz_int.insert(0,0)

gy_int1=gy_int

ax_trimmed = df['x-axis acceleration'].tolist()
ay_trimmed = df['y-axis acceleration'].tolist()
az_trimmed = df['z-axis acceleration'].tolist()

gx_trimmed = df['x-axis gyroscope'].tolist()
gy_trimmed = df['y-axis gyroscope'].tolist()
gz_trimmed = df['z-axis gyroscope'].tolist()

mx_trimmed = df['x-axis magnetometer'].tolist()
my_trimmed = df['y-axis magnetometer'].tolist()
mz_trimmed = df['z-axis magnetometer'].tolist()

t_trimmed = np.arange(0, 7501, 10)
t_trimmed = t_trimmed.tolist()

plt.title('Y-axis gyroscope')
plt.legend(['Angular velocity /s)'])
plt.plot(t_trimmed, gy_trimmed,label='Angular Velocity °/s ')
plt.plot(t_trimmed, gy_int,label='Angular Displacement °')
plt.show()

ax1 = plt.gca()
plt.title('Acceleration Data')
plt.plot(t_trimmed,ax_trimmed,label='X-axis')
plt.plot(t_trimmed,ay_trimmed,label='Y-axis')
plt.plot(t_trimmed,az_trimmed,label='Z-axis')
plt.legend()
plt.show()

ax2 = plt.gca()
plt.title('Gyroscope Data')
plt.plot(t_trimmed,gx_trimmed,label='X-axis')
plt.plot(t_trimmed,gy_trimmed,label='Y-axis')
plt.plot(t_trimmed,gz_trimmed,label='Z-axis')
plt.legend()
plt.show()

ax3 = plt.gca()
plt.title('Magnetometer Data')
plt.plot(t_trimmed,mx_trimmed,label='X-axis')
plt.plot(t_trimmed,my_trimmed,label='Y-axis')
plt.plot(t_trimmed,mz_trimmed,label='Z-axis')
plt.legend()
plt.show()

a4 = plt.gca()

plt.title('Choosing the start point in the graph')
plt.plot(t_trimmed,ax_trimmed,label='X-axis acceleration')
plt.plot(t_trimmed,ay_trimmed,label='Y-axis acceleration')
plt.plot(t_trimmed,az_trimmed,label='Z-axis acceleration')
plt.plot(t_trimmed,mx_trimmed,label='X-axis magnetometer')
plt.plot(t_trimmed,my_trimmed,label='Y-axis magnetometer')
plt.plot(t_trimmed,mz_trimmed,label='Z-axis magnetometer')
plt.plot(t_trimmed,gx_trimmed,label='X-axis gyroscope')
plt.plot(t_trimmed,gy_trimmed,label='Y-axis gyroscope')
plt.plot(t_trimmed,gz_trimmed,label='Z-axis gyroscope')
plt.legend()
plt.show()

read_file1 = pd.read_excel('TD_toenter.xlsx')
df1 = pd.read_excel('TD_toenter.xlsx')
df2=pd.read_excel('TD_osc.xlsx')

gy_int = pd.DataFrame(gy_int)
df2['ID9_meas'] = (gy_int * -1) + 149

df2 = df2[109:]

df2['ID9_meas_trimmed'] = df2['ID9_meas']

ID9_meas_trimmed = df2['ID9_meas_trimmed'].tolist()
ID9_meas_trimmed = [ID9_meas_trimmed for ID9_meas_trimmed in ID9_meas_trimmed if str(ID9_meas_trimmed) != 'nan']

t_trimmed_trimmed = np.arange(0, 6411, 10)

t_trimmed_trimmed = t_trimmed_trimmed.tolist()

ax5 = plt.gca()
plt.title('ID9 entered and Measured values')
plt.plot(t_trimmed_trimmed, ID9_meas_trimmed, label='Measured Angle')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax5, color='red')
plt.legend()
plt.xlabel('Time(ms)')
plt.ylabel('ID9 Servo Angle')
plt.show()

df2 = pd.read_excel('TD_osc_c_1.xlsx')
df['total_gyro_vector'] = df['x-axis gyroscope'] + df['y-axis gyroscope'] + df['z-axis gyroscope']
total_gyro_vector = df['total_gyro_vector'].tolist()

t1 = [a * b for a, b in zip(gx_int, gx_int)]
t2 = [a * b for a, b in zip(gy_int1, gy_int1)]
t3 = [a * b for a, b in zip(gz_int, gz_int)]

total = []

for i in range(0, len(t1)):
    total.append(t1[i] + t2[i]+ t3[i])

total = np.array(total)
total_angle_vector = np.sqrt(total)
total_angle_vector = total_angle_vector.tolist()

t11 = df['x-axis gyroscope'] * df['x-axis gyroscope']
t22 = df['y-axis gyroscope'] * df['y-axis gyroscope']
t33 = df['z-axis gyroscope'] * df['z-axis gyroscope']

total1 = t11 + t22 + t33
df['total_gyro_vector_rms'] = total1 ** (1 / 2)

total_gyro_vector_rms=df['total_gyro_vector_rms'].tolist()




ax6 = plt.gca()
plt.title('TD Gyroscope Measurement')
plt.plot(t_trimmed, total_gyro_vector, label='Angular Velocity °/s')
plt.plot(t_trimmed, total_angle_vector, label='Angular Displacement °')
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.legend()
plt.show()

ax7 = plt.gca()
plt.title('TD Gyroscope Measurement')
plt.plot(t_trimmed,gx_trimmed,label='x-axis Angular Gyroscope')
plt.plot(t_trimmed,gy_trimmed,label='y-axis Angular Gyroscope')
plt.plot(t_trimmed,gz_trimmed,label='z-axis Angular Gyroscope')
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()

ax11 = plt.gca()
plt.title('TD Gyroscope Measurement')
plt.plot(t_trimmed,gy_trimmed,label='Y-axis Angular Gyroscope')
plt.plot(t_trimmed,total_gyro_vector,label='Added Total')
plt.plot(t_trimmed,total_gyro_vector_rms,label='Vector Added Total')
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()

total_angle_vector = pd.DataFrame(total_angle_vector)
ID9_meas_total = (total_angle_vector * -1) + 149

df3 = pd.read_excel('CP_osc.xlsx')
df9=  pd.read_excel('CP_osc.xlsx')
df3['ID9_meas_total'] = ID9_meas_total

df3 = df3[109:]
df3['ID9_meas_trimmed_total'] = ID9_meas_total

ID9_meas_trimmed_total = df3['ID9_meas_trimmed_total'].tolist()
ID9_meas_trimmed_total = [ID9_meas_trimmed_total for ID9_meas_trimmed_total in ID9_meas_trimmed_total if str(ID9_meas_trimmed_total) != 'nan']

ax8 = plt.gca()
plt.title('Servo ID9 Angle')
plt.plot(t_trimmed_trimmed,ID9_meas_trimmed,label='Measured ID9 Angle from Y-axis gyro')
plt.plot(t_trimmed_trimmed,ID9_meas_trimmed_total,label='Measured ID9 Angle from total Gyro Vector')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax8, color='red')
plt.legend()
plt.xlabel('Time(ms)')
plt.ylabel('Angle °')
plt.show()

ax9 = plt.gca()
plt.title('TD Servo ID9 Angle')
plt.plot(t_trimmed_trimmed, ID9_meas_trimmed_total, label='Measured')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax9, color='red')
plt.legend()
plt.show()


ax10 = plt.gca()
plt.title('TD 3-axis Angular Displacement and Vector Sum')
plt.plot(t_trimmed, gx_int, label='X-axis')
plt.plot(t_trimmed, gy_int1, label='y-axis')
plt.plot(t_trimmed, gz_int, label='z-axis')
plt.plot(t_trimmed, total_angle_vector, label='Vector')
plt.xlabel('Time(ms)')
plt.ylabel('Angle °')
plt.legend()
plt.show()

ax11 = plt.gca()
plt.title('TD Gyroscope Raw Data')
plt.plot(t_trimmed, gx_trimmed, label='X-axis gyroscope')
plt.plot(t_trimmed, gy_trimmed, label='X-axis gyroscope')
plt.plot(t_trimmed, gz_trimmed, label='X-axis gyroscope')
plt.xlabel('Time(ms)')
plt.ylabel('Angle °')
plt.legend()
plt.show()

ID9_entered_angle_642element = np.arange(562)

ID9_entered_angle_642element[1] = 149

ID9_entered_angle_642element = ID9_entered_angle_642element.astype('float64')
i = 2
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 95 / 40
    i = i + 1
    if i == 40:
        break
ID9_entered_angle_642element[40] = 54
ID9_entered_angle_642element[41] = 54


i = 42
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 84 / 40
    i = i + 1
    if i == 80:
        break
ID9_entered_angle_642element[80] = 138
ID9_entered_angle_642element[81] = 138
i = 82
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 82 /40
    i = i + 1
    if i == 120:
        break
ID9_entered_angle_642element[120] = 56
ID9_entered_angle_642element[121] = 56
i = 122
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 70 / 40
    i = i + 1
    if i == 160:
        break
ID9_entered_angle_642element[160] = 126
ID9_entered_angle_642element[161] = 126
i = 162
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 67 / 40
    i = i + 1
    if i == 200:
        break
ID9_entered_angle_642element[200] = 59
ID9_entered_angle_642element[201] = 59
i = 202
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 56 / 40
    i = i + 1
    if i == 240:
        break
ID9_entered_angle_642element[240] = 115
ID9_entered_angle_642element[241] = 115
i = 242
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 54 / 40
    i = i + 1
    if i == 280:
        break
ID9_entered_angle_642element[280] = 61
ID9_entered_angle_642element[281] = 61
i = 282
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 43 / 40
    i = i + 1
    if i == 320:
        break
ID9_entered_angle_642element[320] = 104
ID9_entered_angle_642element[321] = 104

i = 322
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 41 / 40
    i = i + 1
    if i == 360:
        break
ID9_entered_angle_642element[360] = 63
ID9_entered_angle_642element[361] = 63
i = 362
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 30 / 40
    i = i + 1
    if i == 400:
        break
ID9_entered_angle_642element[400] = 93
ID9_entered_angle_642element[401] = 93
i = 402
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 28 / 40
    i = i + 1
    if i == 440:
        break
ID9_entered_angle_642element[440] = 65
ID9_entered_angle_642element[441] = 65
i = 442
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 16 / 40
    i = i + 1
    if i == 480:
        break
ID9_entered_angle_642element[480] = 81
ID9_entered_angle_642element[481] = 81
i = 482
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] - 13 / 40
    i = i + 1
    if i == 520:
        break
ID9_entered_angle_642element[520] = 68
ID9_entered_angle_642element[521] = 68
i = 522
while ID9_entered_angle_642element[i] < ID9_entered_angle_642element.size:
    ID9_entered_angle_642element[i] = ID9_entered_angle_642element[i - 1] + 2 / 40
    i = i + 1
    if i == 560:
        break
ID9_entered_angle_642element[560] =70
ID9_entered_angle_642element[561] = 70


End_70s_a = 70 * np.ones(81)
End_70s_a = End_70s_a.tolist()
ID9_entered_angle_642element = ID9_entered_angle_642element.tolist()

ID9_entered_angle_642element.pop(0)

ID9_entered_angle_642element_final = ID9_entered_angle_642element + End_70s_a

ax12 = plt.gca()

plt.title('Test Plot')
df1.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax12)
plt.plot(t_trimmed_trimmed,ID9_entered_angle_642element_final)
plt.xlabel('Time (ms)')
plt.ylabel('Angle ')
plt.show()

R=np.corrcoef(ID9_entered_angle_642element_final, ID9_meas_trimmed_total)
from sklearn.metrics import mean_squared_error
from math import sqrt


RMSE = sqrt(mean_squared_error(ID9_entered_angle_642element_final, ID9_meas_trimmed_total))
RMSE1 = sqrt(mean_squared_error(ID9_entered_angle_642element_final, ID9_meas_trimmed))