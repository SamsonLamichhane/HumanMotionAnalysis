import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from decimal import *
import numpy as np
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
import statistics
from array import *

read_file = pd.read_excel('still_xz2.xlsx')
df = pd.read_excel('still_xz2.xlsx')

df["x-axis acceleration"] = pd.to_numeric(df["x-axis acceleration"], downcast="float")
df["x-axis acceleration"] = ((df["x-axis acceleration"] * 9.81) / 8192)

df["y-axis acceleration"] = pd.to_numeric(df["y-axis acceleration"], downcast="float")
df["y-axis acceleration"] = ((df["y-axis acceleration"] * 9.81) / 8192)

df["z-axis acceleration"] = pd.to_numeric(df["z-axis acceleration"], downcast="float")
df["z-axis acceleration"] = ((df["z-axis acceleration"] * 9.81) / 8192)

df["x-axis gyroscope"] = pd.to_numeric(df["x-axis gyroscope"], downcast="float")
df["x-axis gyroscope"] = (df["x-axis gyroscope"] / 16.4)

df["y-axis gyroscope"] = pd.to_numeric(df["y-axis gyroscope"], downcast="float")
df["y-axis gyroscope"] = (df["y-axis gyroscope"] / 16.4)

df["z-axis gyroscope"] = pd.to_numeric(df["z-axis gyroscope"], downcast="float")
df["z-axis gyroscope"] = (df["z-axis gyroscope"] / 16.4)

df["x-axis magnetometer"] = pd.to_numeric(df["x-axis magnetometer"], downcast="float")
df["x-axis magnetometer"] = (df["x-axis magnetometer"] * 0.6)

df["y-axis magnetometer"] = pd.to_numeric(df["y-axis magnetometer"], downcast="float")
df["y-axis magnetometer"] = (df["y-axis magnetometer"] * 0.6)

df["z-axis magnetometer"] = pd.to_numeric(df["z-axis magnetometer"], downcast="float")
df["z-axis magnetometer"] = (df["z-axis magnetometer"] * 0.6)

ax = df['x-axis acceleration'].tolist()
ay = df['y-axis acceleration'].tolist()
az = df['z-axis acceleration'].tolist()

gx = df['x-axis gyroscope'].tolist()
gy = df['y-axis gyroscope'].tolist()
gz = df['z-axis gyroscope'].tolist()

t = df['Time (ms)'].tolist()

startPoint = 1
windowBefore = 0
windowAfter = 999

df = df[startPoint - windowBefore - 1:startPoint + windowAfter]

gx_int = integrate.cumtrapz(df['x-axis gyroscope'], dx=0.01)
gy_int = integrate.cumtrapz(df['y-axis gyroscope'], dx=0.01)
gz_int = integrate.cumtrapz(df['z-axis gyroscope'], dx=0.01)

gx_int = gx_int.tolist()
gy_int = gy_int.tolist()
gz_int = gz_int.tolist()

gx_int.insert(0, 0)
gy_int.insert(0, 0)
gz_int.insert(0, 0)

ax_trimmed = df['x-axis acceleration'].tolist()
ay_trimmed = df['y-axis acceleration'].tolist()
az_trimmed = df['z-axis acceleration'].tolist()

gx_trimmed = df['x-axis gyroscope'].tolist()
gy_trimmed = df['y-axis gyroscope'].tolist()
gz_trimmed = df['z-axis gyroscope'].tolist()

mx_trimmed = df['x-axis magnetometer'].tolist()
my_trimmed = df['y-axis magnetometer'].tolist()
mz_trimmed = df['z-axis magnetometer'].tolist()

t_trimmed = df['Time (ms)'].tolist()

DatabasePoint = 104

t1 = [a * b for a, b in zip(gx_int, gx_int)]
t2 = [a * b for a, b in zip(gy_int, gy_int)]
t3 = [a * b for a, b in zip(gz_int, gz_int)]

total = []

for i in range(0, len(t1)):
    total.append(t1[i] + t2[i] + t3[i])

total = np.array(total)
total_angle_vector = np.sqrt(total)
total_angle_vector = total_angle_vector
ID9_meas_total = (total_angle_vector * -1) + 140

ID9_meas_total = pd.DataFrame(ID9_meas_total)

df2 = pd.read_excel('still_xz2.xlsx')

df2['ID9_meas_total'] = ID9_meas_total
df2 = df2[103:]

ID9_meas_trimmed_total = df2['ID9_meas_total'].tolist()
t_trimmed_trimmed = np.arange(0, 2431, 10)

t_trimmed_trimmed = t_trimmed_trimmed.tolist()

mean_xGyro = statistics.mean(gx)
mean_yGyro = statistics.mean(gy)
mean_zGyro = statistics.mean(gz)

mean_x = mean_xGyro * np.ones(1000)
mean_x = mean_x.tolist()

mean_y = mean_yGyro * np.ones(1000)
mean_y = mean_y.tolist()

mean_z = mean_zGyro * np.ones(1000)
mean_z = mean_z.tolist()

gx = np.asarray(gx)
length_gx = (len(gx))

gx_comp = np.arange(length_gx)
gx_comp = gx_comp.astype('float64')

for i in range(len(gx)):
    gx_comp[i] = gx[i] - mean_xGyro

gy = np.asarray(gy)
length_gy = (len(gy))

gy_comp = np.arange(length_gy)
gy_comp = gy_comp.astype('float64')

for i in range(len(gy)):
    gy_comp[i] = gy[i] - mean_yGyro

gz = np.asarray(gz)
length_gz = (len(gz))
gz_comp = np.arange(length_gz)
gz_comp = gz_comp.astype('float64')
for i in range(len(gz)):
    gz_comp[i] = gz[i] - mean_zGyro

gx_comp = gx_comp.tolist()
gy_comp = gy_comp.tolist()
gz_comp = gz_comp.tolist()


gx_comp_int = integrate.cumtrapz(gx_comp, dx=0.01)
gy_comp_int = integrate.cumtrapz(gy_comp, dx=0.01)
gz_comp_int = integrate.cumtrapz(gz_comp, dx=0.01)

gx_comp_int=gx_comp_int.tolist()
gy_comp_int=gy_comp_int.tolist()
gz_comp_int=gz_comp_int.tolist()

gx_comp_int.insert(0, 0)
gy_comp_int.insert(0, 0)
gz_comp_int.insert(0, 0)

axes = plt.gca()
axes.set_ylim([-2, 0.5])
plt.title('Still Trial for XZ Plane')
plt.plot(t, gx, label='X-axis gyroscope')
plt.plot(t, mean_x, label='Average Data Value')
plt.xlabel('Time (ms)')
plt.ylabel('Angular Veloctiy °/s')
plt.legend()
plt.show()

axes1 = plt.gca()
axes1.set_ylim([-2, 0.5])
plt.title('Still Trial for XZ Plane')
plt.plot(t, gy, label='Y-axis gyroscope')
plt.plot(t, mean_y, label='Average Data Value')
plt.xlabel('Time (ms)')
plt.ylabel('Angular Veloctiy °/s')
plt.legend()
plt.show()

axes2 = plt.gca()
axes2.set_ylim([-2, 0.5])
plt.title('Still Trial for XZ Plane')
plt.plot(t, gz, label='Z-axis gyroscope')
plt.plot(t, mean_z, label='Average Data Value')
plt.xlabel('Time (ms)')
plt.ylabel('Angular Veloctiy °/s')
plt.legend()
plt.show()

axes3 = plt.gca()
plt.title('Still Trial for XZ Plane')
plt.plot(t, gx_int, label='Uncalibrated X-axis')
plt.plot(t, gx_comp_int, label='Calibrated X-axis')
plt.xlabel('Time (ms)')
plt.ylabel('Angular °')
plt.legend()
plt.show()

axes4 = plt.gca()
plt.title('Still Trial for XZ Plane')
plt.plot(t, gy_int, label='Uncalibrated Y-axis')
plt.plot(t, gy_comp_int, label='Calibrated Y-axis')
plt.xlabel('Time (ms)')
plt.ylabel('Angular °')
plt.legend()
plt.show()

axes5 = plt.gca()
plt.title('Still Trial for XZ Plane')
plt.plot(t, gz_int, label='Uncalibrated Z-axis')
plt.plot(t, gz_comp_int, label='Calibrated Z-axis')
plt.xlabel('Time (ms)')
plt.ylabel('Angular °')
plt.legend()
plt.show()


