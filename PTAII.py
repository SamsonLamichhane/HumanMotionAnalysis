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

startPoint_TD = 250
startPoint_TD_c = 295

windowBefore_TD = 100
windowAfter_TD = 650


startPoint_CP = 382
startPoint_CP_c = 290

windowBefore_CP = 100
windowAfter_CP = 300

read_file = pd.read_excel('TD_osc.xlsx')
df = pd.read_excel('TD_osc.xlsx')

df["x-axis gyroscope"] = pd.to_numeric(df["x-axis gyroscope"], downcast="float")
df["x-axis gyroscope"] = (df["x-axis gyroscope"] / 16.4)

df["y-axis gyroscope"] = pd.to_numeric(df["y-axis gyroscope"], downcast="float")
df["y-axis gyroscope"] = (df["y-axis gyroscope"] / 16.4)

df["z-axis gyroscope"] = pd.to_numeric(df["z-axis gyroscope"], downcast="float")
df["z-axis gyroscope"] = (df["z-axis gyroscope"] / 16.4)

xGyroOffset = -0.088976965
yGyroOffset = -0.753604336
zGyroOffset = -1.248733062

df["gx_TD_nc_uncomp"] = df['x-axis gyroscope']
df["gy_TD_nc_uncomp"] = df['y-axis gyroscope']
df["gz_TD_nc_uncomp"] = df['z-axis gyroscope']

df["gx_TD_nc_comp"] = df['x-axis gyroscope'] - xGyroOffset
df["gy_TD_nc_comp"] = df['y-axis gyroscope'] - yGyroOffset
df["gz_TD_nc_comp"] = df['z-axis gyroscope'] - zGyroOffset


df = df[startPoint_TD-windowBefore_TD-1: startPoint_TD+windowAfter_TD]

df["gx_TD_nc_uncomp_trimmed"]=df["gx_TD_nc_uncomp"]
df["gy_TD_nc_uncomp_trimmed"]=df["gy_TD_nc_uncomp"]
df["gz_TD_nc_uncomp_trimmed"]=df["gz_TD_nc_uncomp"]

df["gx_TD_nc_comp_trimmed"]=df["gx_TD_nc_comp"]
df["gy_TD_nc_comp_trimmed"]=df["gy_TD_nc_comp"]
df["gz_TD_nc_comp_trimmed"]=df["gz_TD_nc_comp"]

gx_TD_nc_uncomp_int = integrate.cumtrapz(df['gx_TD_nc_uncomp_trimmed'], dx=0.01)
gy_TD_nc_uncomp_int = integrate.cumtrapz(df['gy_TD_nc_uncomp_trimmed'], dx=0.01)
gz_TD_nc_uncomp_int = integrate.cumtrapz(df['gz_TD_nc_uncomp_trimmed'], dx=0.01)

gx_TD_nc_comp_int = integrate.cumtrapz(df['gx_TD_nc_comp_trimmed'], dx=0.01)
gy_TD_nc_comp_int = integrate.cumtrapz(df['gy_TD_nc_comp_trimmed'], dx=0.01)
gz_TD_nc_comp_int = integrate.cumtrapz(df['gz_TD_nc_comp_trimmed'], dx=0.01)

gx_TD_nc_uncomp_int = gx_TD_nc_uncomp_int.tolist()
gy_TD_nc_uncomp_int = gy_TD_nc_uncomp_int.tolist()
gz_TD_nc_uncomp_int = gz_TD_nc_uncomp_int.tolist()

gx_TD_nc_comp_int = gx_TD_nc_comp_int.tolist()
gy_TD_nc_comp_int = gy_TD_nc_comp_int.tolist()
gz_TD_nc_comp_int = gz_TD_nc_comp_int.tolist()

gx_TD_nc_uncomp_int.insert(0,0)
gy_TD_nc_uncomp_int.insert(0,0)
gz_TD_nc_uncomp_int.insert(0,0)

gx_TD_nc_comp_int.insert(0,0)
gy_TD_nc_comp_int.insert(0,0)
gz_TD_nc_comp_int.insert(0,0)

databasepoint_TD_nc = 111

df1 = pd.read_excel('TD_osc.xlsx')

t1 = [a * b for a, b in zip(gx_TD_nc_uncomp_int, gx_TD_nc_uncomp_int)]
t2 = [a * b for a, b in zip(gy_TD_nc_uncomp_int, gy_TD_nc_uncomp_int)]
t3 = [a * b for a, b in zip(gz_TD_nc_uncomp_int, gz_TD_nc_uncomp_int)]

total = []

for i in range(0, len(t1)):
    total.append(t1[i] + t2[i] + t3[i])

total = np.array(total)
vector_TD_nc_uncomp = np.sqrt(total)

ID9_TD_nc_uncomp_preTrim = (vector_TD_nc_uncomp*-1)+149
vector_TD_nc_uncomp = vector_TD_nc_uncomp.tolist()
t11 = [a * b for a, b in zip(gx_TD_nc_comp_int, gx_TD_nc_comp_int)]
t21 = [a * b for a, b in zip(gy_TD_nc_comp_int, gy_TD_nc_comp_int)]
t31 = [a * b for a, b in zip(gz_TD_nc_comp_int, gz_TD_nc_comp_int)]


total1 = []

for i in range(0, len(t11)):
    total1.append(t11[i] + t21[i] + t31[i])

total1 = np.array(total1)
vector_TD_nc_comp = np.sqrt(total1)

ID9_TD_nc_comp_preTrim = (vector_TD_nc_comp*-1)+149

ID9_TD_nc_comp_preTrim = pd.DataFrame(ID9_TD_nc_comp_preTrim)

df1['ID9_TD_nc_comp_preTrim'] = ID9_TD_nc_comp_preTrim
vector_TD_nc_comp = vector_TD_nc_comp.tolist()

ID9_TD_nc_uncomp_preTrim = pd.DataFrame(ID9_TD_nc_uncomp_preTrim)




df1['ID9_TD_nc_uncomp_preTrim'] = ID9_TD_nc_uncomp_preTrim



df1 = df1[databasepoint_TD_nc - 1:]

df1['ID9_TD_nc_uncomp'] = df1['ID9_TD_nc_uncomp_preTrim']

df1['ID9_TD_nc_comp'] = df1['ID9_TD_nc_comp_preTrim']

ID9_TD_nc_uncomp = df1['ID9_TD_nc_uncomp'].tolist()
ID9_TD_nc_comp = df1['ID9_TD_nc_comp'].tolist()


################WITHCASE###################

read_file2 = pd.read_excel('TD_osc_c.xlsx')
df2 = pd.read_excel('TD_osc_c.xlsx')

df2["x-axis gyroscope"] = pd.to_numeric(df2["x-axis gyroscope"], downcast="float")
df2["x-axis gyroscope"] = (df2["x-axis gyroscope"] / 16.4)

df2["y-axis gyroscope"] = pd.to_numeric(df2["y-axis gyroscope"], downcast="float")
df2["y-axis gyroscope"] = (df2["y-axis gyroscope"] / 16.4)

df2["z-axis gyroscope"] = pd.to_numeric(df2["z-axis gyroscope"], downcast="float")
df2["z-axis gyroscope"] = (df2["z-axis gyroscope"] / 16.4)



df2["gx_TD_c_uncomp"] = df2['x-axis gyroscope']
df2["gy_TD_c_uncomp"] = df2['y-axis gyroscope']
df2["gz_TD_c_uncomp"] = df2['z-axis gyroscope']

df2["gx_TD_c_comp"] = df2['x-axis gyroscope'] - xGyroOffset
df2["gy_TD_c_comp"] = df2['y-axis gyroscope'] - yGyroOffset
df2["gz_TD_c_comp"] = df2['z-axis gyroscope'] - zGyroOffset


df2 = df2[startPoint_TD_c-windowBefore_TD-1: startPoint_TD_c+windowAfter_TD]

df2["gx_TD_c_uncomp_trimmed"]=df2["gx_TD_c_uncomp"]
df2["gy_TD_c_uncomp_trimmed"]=df2["gy_TD_c_uncomp"]
df2["gz_TD_c_uncomp_trimmed"]=df2["gz_TD_c_uncomp"]

df2["gx_TD_c_comp_trimmed"]=df2["gx_TD_c_comp"]
df2["gy_TD_c_comp_trimmed"]=df2["gy_TD_c_comp"]
df2["gz_TD_c_comp_trimmed"]=df2["gz_TD_c_comp"]

gx_TD_c_uncomp_int = integrate.cumtrapz(df2['gx_TD_c_uncomp_trimmed'], dx=0.01)
gy_TD_c_uncomp_int = integrate.cumtrapz(df2['gy_TD_c_uncomp_trimmed'], dx=0.01)
gz_TD_c_uncomp_int = integrate.cumtrapz(df2['gz_TD_c_uncomp_trimmed'], dx=0.01)

gx_TD_c_comp_int = integrate.cumtrapz(df2['gx_TD_c_comp_trimmed'], dx=0.01)
gy_TD_c_comp_int = integrate.cumtrapz(df2['gy_TD_c_comp_trimmed'], dx=0.01)
gz_TD_c_comp_int = integrate.cumtrapz(df2['gz_TD_c_comp_trimmed'], dx=0.01)

gx_TD_c_uncomp_int = gx_TD_c_uncomp_int.tolist()
gy_TD_c_uncomp_int = gy_TD_c_uncomp_int.tolist()
gz_TD_c_uncomp_int = gz_TD_c_uncomp_int.tolist()

gx_TD_c_comp_int = gx_TD_c_comp_int.tolist()
gy_TD_c_comp_int = gy_TD_c_comp_int.tolist()
gz_TD_c_comp_int = gz_TD_c_comp_int.tolist()

gx_TD_c_uncomp_int.insert(0,0)
gy_TD_c_uncomp_int.insert(0,0)
gz_TD_c_uncomp_int.insert(0,0)

gx_TD_c_comp_int.insert(0,0)
gy_TD_c_comp_int.insert(0,0)
gz_TD_c_comp_int.insert(0,0)

databasepoint_TD_c = 106

df3 = pd.read_excel('TD_osc_c.xlsx')

t1a = [a * b for a, b in zip(gx_TD_c_uncomp_int, gx_TD_c_uncomp_int)]
t2a = [a * b for a, b in zip(gy_TD_c_uncomp_int, gy_TD_c_uncomp_int)]
t3a = [a * b for a, b in zip(gz_TD_c_uncomp_int, gz_TD_c_uncomp_int)]

totala = []

for i in range(0, len(t1a)):
    totala.append(t1a[i] + t2a[i] + t3a[i])

totala = np.array(totala)
vector_TD_c_uncomp = np.sqrt(totala)

ID9_TD_c_uncomp_preTrim = (vector_TD_c_uncomp*-1)+149

vector_TD_c_uncomp = vector_TD_c_uncomp.tolist()

t11a = [a * b for a, b in zip(gx_TD_c_comp_int, gx_TD_c_comp_int)]
t21a = [a * b for a, b in zip(gy_TD_c_comp_int, gy_TD_c_comp_int)]
t31a = [a * b for a, b in zip(gz_TD_c_comp_int, gz_TD_c_comp_int)]

total1a = []

for i in range(0, len(t11a)):
    total1a.append(t11a[i] + t21a[i] + t31a[i])

total1a = np.array(total1a)
vector_TD_c_comp = np.sqrt(total1a)

ID9_TD_c_comp_preTrim = (vector_TD_c_comp*-1)+149

vector_TD_c_comp = vector_TD_c_comp.tolist()

ID9_TD_c_comp_preTrim = pd.DataFrame(ID9_TD_c_comp_preTrim)
ID9_TD_c_uncomp_preTrim = pd.DataFrame(ID9_TD_c_uncomp_preTrim)

df3['ID9_TD_c_uncomp_preTrim']=ID9_TD_c_uncomp_preTrim
df3['ID9_TD_c_comp_preTrim']=ID9_TD_c_comp_preTrim

df3 = df3[databasepoint_TD_c - 1:]


df3['ID9_TD_c_uncomp'] = df3['ID9_TD_c_uncomp_preTrim']

df3['ID9_TD_c_comp'] = df3['ID9_TD_c_comp_preTrim']

ID9_TD_c_uncomp = df3['ID9_TD_c_uncomp'].tolist()
ID9_TD_c_comp = df3['ID9_TD_c_comp'].tolist()

      #########################################CPDATA#######################



read_file = pd.read_excel('CP_osc.xlsx')
df4 = pd.read_excel('CP_osc.xlsx')

df4["x-axis gyroscope"] = pd.to_numeric(df4["x-axis gyroscope"], downcast="float")
df4["x-axis gyroscope"] = (df4["x-axis gyroscope"] / 16.4)

df4["y-axis gyroscope"] = pd.to_numeric(df4["y-axis gyroscope"], downcast="float")
df4["y-axis gyroscope"] = (df4["y-axis gyroscope"] / 16.4)

df4["z-axis gyroscope"] = pd.to_numeric(df4["z-axis gyroscope"], downcast="float")
df4["z-axis gyroscope"] = (df4["z-axis gyroscope"] / 16.4)

df4["gx_CP_nc_uncomp"] = df4['x-axis gyroscope']
df4["gy_CP_nc_uncomp"] = df4['y-axis gyroscope']
df4["gz_CP_nc_uncomp"] = df4['z-axis gyroscope']

df4["gx_CP_nc_comp"] = df4['x-axis gyroscope'] - xGyroOffset
df4["gy_CP_nc_comp"] = df4['y-axis gyroscope'] - yGyroOffset
df4["gz_CP_nc_comp"] = df4['z-axis gyroscope'] - zGyroOffset


df4 = df4[startPoint_CP-windowBefore_CP-1: startPoint_CP+windowAfter_CP]

df4["gx_CP_nc_uncomp_trimmed"]=df4["gx_CP_nc_uncomp"]
df4["gy_CP_nc_uncomp_trimmed"]=df4["gy_CP_nc_uncomp"]
df4["gz_CP_nc_uncomp_trimmed"]=df4["gz_CP_nc_uncomp"]

df4["gx_CP_nc_comp_trimmed"]=df4["gx_CP_nc_comp"]
df4["gy_CP_nc_comp_trimmed"]=df4["gy_CP_nc_comp"]
df4["gz_CP_nc_comp_trimmed"]=df4["gz_CP_nc_comp"]

gx_CP_nc_uncomp_int = integrate.cumtrapz(df4['gx_CP_nc_uncomp_trimmed'], dx=0.01)
gy_CP_nc_uncomp_int = integrate.cumtrapz(df4['gy_CP_nc_uncomp_trimmed'], dx=0.01)
gz_CP_nc_uncomp_int = integrate.cumtrapz(df4['gz_CP_nc_uncomp_trimmed'], dx=0.01)

gx_CP_nc_comp_int = integrate.cumtrapz(df4['gx_CP_nc_comp_trimmed'], dx=0.01)
gy_CP_nc_comp_int = integrate.cumtrapz(df4['gy_CP_nc_comp_trimmed'], dx=0.01)
gz_CP_nc_comp_int = integrate.cumtrapz(df4['gz_CP_nc_comp_trimmed'], dx=0.01)

gx_CP_nc_uncomp_int = gx_CP_nc_uncomp_int.tolist()
gy_CP_nc_uncomp_int = gy_CP_nc_uncomp_int.tolist()
gz_CP_nc_uncomp_int = gz_CP_nc_uncomp_int.tolist()

gx_CP_nc_comp_int = gx_CP_nc_comp_int.tolist()
gy_CP_nc_comp_int = gy_CP_nc_comp_int.tolist()
gz_CP_nc_comp_int = gz_CP_nc_comp_int.tolist()

gx_CP_nc_uncomp_int.insert(0,0)
gy_CP_nc_uncomp_int.insert(0,0)
gz_CP_nc_uncomp_int.insert(0,0)

gx_CP_nc_comp_int.insert(0,0)
gy_CP_nc_comp_int.insert(0,0)
gz_CP_nc_comp_int.insert(0,0)




databasepoint_CP_nc = 104

df5 = pd.read_excel('CP_osc.xlsx')

t1c = [a * b for a, b in zip(gx_CP_nc_uncomp_int, gx_CP_nc_uncomp_int)]
t2c = [a * b for a, b in zip(gy_CP_nc_uncomp_int, gy_CP_nc_uncomp_int)]
t3c = [a * b for a, b in zip(gz_CP_nc_uncomp_int, gz_CP_nc_uncomp_int)]

totalc = []

for i in range(0, len(t1c)):
    totalc.append(t1c[i] + t2c[i] + t3c[i])

totalc = np.array(totalc)
vector_CP_nc_uncomp = np.sqrt(totalc)

ID9_CP_nc_uncomp_preTrim = (vector_CP_nc_uncomp*-1)+135


vector_CP_nc_uncomp = vector_CP_nc_uncomp.tolist()
t11c = [a * b for a, b in zip(gx_CP_nc_comp_int, gx_CP_nc_comp_int)]
t21c = [a * b for a, b in zip(gy_CP_nc_comp_int, gy_CP_nc_comp_int)]
t31c = [a * b for a, b in zip(gz_CP_nc_comp_int, gz_CP_nc_comp_int)]

t_CP_nc_trimmed = np.arange(0,4010,10)
t_CP_nc_trimmed = t_CP_nc_trimmed.tolist()

t_CP_nc_trimmed2= np.arange(0,2980,10)
t_CP_nc_trimmed2 = t_CP_nc_trimmed2.tolist()


t_CP_c_trimmed = np.arange(0,4010,10)
t_CP_c_trimmed = t_CP_c_trimmed.tolist()

t_CP_c_trimmed2= np.arange(0,2960,10)
t_CP_c_trimmed2 = t_CP_c_trimmed2.tolist()




total1c = []

for i in range(0, len(t11c)):
    total1c.append(t11c[i] + t21c[i] + t31c[i])

total1c = np.array(total1c)
vector_CP_nc_comp = np.sqrt(total1c)

ID9_CP_nc_comp_preTrim = (vector_CP_nc_comp*-1)+135

ID9_CP_nc_comp_preTrim = pd.DataFrame(ID9_CP_nc_comp_preTrim)

df5['ID9_CP_nc_comp_preTrim'] = ID9_CP_nc_comp_preTrim
vector_CP_nc_comp = vector_CP_nc_comp.tolist()

ID9_CP_nc_uncomp_preTrim = pd.DataFrame(ID9_CP_nc_uncomp_preTrim)

df5['ID9_CP_nc_uncomp_preTrim'] = ID9_CP_nc_uncomp_preTrim


df5 = df5[databasepoint_CP_nc - 1:]

df5['ID9_CP_nc_uncomp'] = df5['ID9_CP_nc_uncomp_preTrim']

df5['ID9_CP_nc_comp'] = df5['ID9_CP_nc_comp_preTrim']

ID9_CP_nc_uncomp = df5['ID9_CP_nc_uncomp'].tolist()
ID9_CP_nc_comp = df5['ID9_CP_nc_comp'].tolist()

################WITHCASE###################

read_file2a = pd.read_excel('CP_osc_c.xlsx')
df6 = pd.read_excel('CP_osc_c.xlsx')

df6["x-axis gyroscope"] = pd.to_numeric(df6["x-axis gyroscope"], downcast="float")
df6["x-axis gyroscope"] = (df6["x-axis gyroscope"] / 16.4)

df6["y-axis gyroscope"] = pd.to_numeric(df6["y-axis gyroscope"], downcast="float")
df6["y-axis gyroscope"] = (df6["y-axis gyroscope"] / 16.4)

df6["z-axis gyroscope"] = pd.to_numeric(df6["z-axis gyroscope"], downcast="float")
df6["z-axis gyroscope"] = (df6["z-axis gyroscope"] / 16.4)

df6["gx_CP_c_uncomp"] = df6['x-axis gyroscope']
df6["gy_CP_c_uncomp"] = df6['y-axis gyroscope']
df6["gz_CP_c_uncomp"] = df6['z-axis gyroscope']

df6["gx_CP_c_comp"] = df6['x-axis gyroscope'] - xGyroOffset
df6["gy_CP_c_comp"] = df6['y-axis gyroscope'] - yGyroOffset
df6["gz_CP_c_comp"] = df6['z-axis gyroscope'] - zGyroOffset



df6 = df6[startPoint_CP_c-windowBefore_CP-1: startPoint_CP_c+windowAfter_CP]

df6["gx_CP_c_uncomp_trimmed"]=df6["gx_CP_c_uncomp"]
df6["gy_CP_c_uncomp_trimmed"]=df6["gy_CP_c_uncomp"]
df6["gz_CP_c_uncomp_trimmed"]=df6["gz_CP_c_uncomp"]

df6["gx_CP_c_comp_trimmed"]=df6["gx_CP_c_comp"]
df6["gy_CP_c_comp_trimmed"]=df6["gy_CP_c_comp"]
df6["gz_CP_c_comp_trimmed"]=df6["gz_CP_c_comp"]

gx_CP_c_uncomp_int = integrate.cumtrapz(df6['gx_CP_c_uncomp_trimmed'], dx=0.01)
gy_CP_c_uncomp_int = integrate.cumtrapz(df6['gy_CP_c_uncomp_trimmed'], dx=0.01)
gz_CP_c_uncomp_int = integrate.cumtrapz(df6['gz_CP_c_uncomp_trimmed'], dx=0.01)

gx_CP_c_comp_int = integrate.cumtrapz(df6['gx_CP_c_comp_trimmed'], dx=0.01)
gy_CP_c_comp_int = integrate.cumtrapz(df6['gy_CP_c_comp_trimmed'], dx=0.01)
gz_CP_c_comp_int = integrate.cumtrapz(df6['gz_CP_c_comp_trimmed'], dx=0.01)

gx_CP_c_uncomp_int = gx_CP_c_uncomp_int.tolist()
gy_CP_c_uncomp_int = gy_CP_c_uncomp_int.tolist()
gz_CP_c_uncomp_int = gz_CP_c_uncomp_int.tolist()

gx_CP_c_comp_int = gx_CP_c_comp_int.tolist()
gy_CP_c_comp_int = gy_CP_c_comp_int.tolist()
gz_CP_c_comp_int = gz_CP_c_comp_int.tolist()

gx_CP_c_uncomp_int.insert(0,0)
gy_CP_c_uncomp_int.insert(0,0)
gz_CP_c_uncomp_int.insert(0,0)

gx_CP_c_comp_int.insert(0,0)
gy_CP_c_comp_int.insert(0,0)
gz_CP_c_comp_int.insert(0,0)

databasepoint_CP_c = 106

df7 = pd.read_excel('TD_osc_c.xlsx')

t1aa = [a * b for a, b in zip(gx_CP_c_uncomp_int, gx_CP_c_uncomp_int)]
t2aa= [a * b for a, b in zip(gy_CP_c_uncomp_int, gy_CP_c_uncomp_int)]
t3aa = [a * b for a, b in zip(gz_CP_c_uncomp_int, gz_CP_c_uncomp_int)]

totalaa = []

for i in range(0, len(t1aa)):
    totalaa.append(t1aa[i] + t2aa[i] + t3aa[i])

totalaa = np.array(totalaa)
vector_CP_c_uncomp = np.sqrt(totalaa)

ID9_CP_c_uncomp_preTrim = (vector_CP_c_uncomp*-1)+135

vector_CP_c_uncomp = vector_CP_c_uncomp.tolist()

t11aa = [a * b for a, b in zip(gx_CP_c_comp_int, gx_CP_c_comp_int)]
t21aa = [a * b for a, b in zip(gy_CP_c_comp_int, gy_CP_c_comp_int)]
t31aa = [a * b for a, b in zip(gz_CP_c_comp_int, gz_CP_c_comp_int)]

total1aa = []

for i in range(0, len(t11aa)):
    total1aa.append(t11aa[i] + t21aa[i] + t31aa[i])

total1aa = np.array(total1aa)
vector_CP_c_comp = np.sqrt(total1aa)

ID9_CP_c_comp_preTrim = (vector_CP_c_comp*-1)+135

vector_CP_c_comp = vector_CP_c_comp.tolist()

ID9_CP_c_comp_preTrim = pd.DataFrame(ID9_CP_c_comp_preTrim)
ID9_CP_c_uncomp_preTrim = pd.DataFrame(ID9_CP_c_uncomp_preTrim)

df7['ID9_CP_c_uncomp_preTrim']=ID9_CP_c_uncomp_preTrim
df7['ID9_CP_c_comp_preTrim']=ID9_CP_c_comp_preTrim

df7 = df7[databasepoint_CP_c - 1:]


df7['ID9_CP_c_uncomp'] = df7['ID9_CP_c_uncomp_preTrim']

df7['ID9_CP_c_comp'] = df7['ID9_CP_c_comp_preTrim']

ID9_CP_c_uncomp = df7['ID9_CP_c_uncomp'].tolist()
ID9_CP_c_comp = df7['ID9_CP_c_comp'].tolist()

read_file8 = pd.read_excel('CP_toenter.xlsx')
df8 = pd.read_excel('CP_toenter.xlsx')
read_file9 = pd.read_excel('TD_toenter.xlsx')
df9 = pd.read_excel('TD_toenter.xlsx')


t_TD_nc_trimmed = np.arange(0,7510,10)
t_TD_nc_trimmed = t_TD_nc_trimmed.tolist()

t_TD_nc_trimmed2= np.arange(0,6410,10)
t_TD_nc_trimmed2 = t_TD_nc_trimmed2.tolist()

t_TD_c_trimmed = np.arange(0,6410,10)
t_TD_c_trimmed = t_TD_c_trimmed.tolist()

t_TD_c_trimmed2= np.arange(0,6460,10)
t_TD_c_trimmed2 = t_TD_c_trimmed2.tolist()

ID9_TD_nc_uncomp = [ID9_TD_nc_uncomp for ID9_TD_nc_uncomp in ID9_TD_nc_uncomp if str(ID9_TD_nc_uncomp)!='nan']
ID9_TD_nc_comp = [ID9_TD_nc_comp for ID9_TD_nc_comp in ID9_TD_nc_comp if str(ID9_TD_nc_comp)!='nan']

ID9_TD_c_uncomp = [ID9_TD_c_uncomp for ID9_TD_c_uncomp in ID9_TD_c_uncomp if str(ID9_TD_c_uncomp)!='nan']
ID9_TD_c_comp = [ID9_TD_c_comp for ID9_TD_c_comp in ID9_TD_c_comp if str(ID9_TD_c_comp)!='nan']

ID9_CP_nc_uncomp = [ID9_CP_nc_uncomp for ID9_CP_nc_uncomp in ID9_CP_nc_uncomp if str(ID9_CP_nc_uncomp)!='nan']
ID9_CP_nc_comp = [ID9_CP_nc_comp for ID9_CP_nc_comp in ID9_CP_nc_comp if str(ID9_CP_nc_comp)!='nan']



ID9_CP_c_uncomp = [ID9_CP_c_uncomp for ID9_CP_c_uncomp in ID9_CP_c_uncomp if str(ID9_CP_c_uncomp)!='nan']
ID9_CP_c_comp = [ID9_CP_c_comp for ID9_CP_c_comp in ID9_CP_c_comp if str(ID9_CP_c_comp)!='nan']


ax1 = plt.gca()
plt.title('Alpha 1 Pendulum Test Angle Measurements ( UNCOMPENSATED')
df9.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax1, color='brown')
plt.plot(t_TD_nc_trimmed2,ID9_TD_nc_uncomp)
plt.plot(t_TD_c_trimmed2,ID9_TD_c_uncomp)
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()

ax2 = plt.gca()
plt.title('Alpha 1 Pendulum Test Angle Measurements (COMPENSATED)')
df9.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax2, color='brown')
plt.plot(t_TD_nc_trimmed2,ID9_TD_nc_comp)
plt.plot(t_TD_c_trimmed2,ID9_TD_c_comp)
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()


ax3 = plt.gca()
plt.title('Alpha 1 Pendulum Test Angle Measurements ( UNCOMPENSATED')
df8.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax3, color='brown')
plt.plot(t_CP_nc_trimmed2,ID9_CP_nc_uncomp)
plt.plot(t_CP_c_trimmed2,ID9_CP_c_uncomp)
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()

ax4 = plt.gca()
plt.title('Alpha 1 Pendulum Test Angle Measurements (COMPENSATED)')
df8.plot(kind='line', x='ID9_entered_time', y='ID9_entered_angle', ax=ax4, color='brown')
plt.plot(t_CP_nc_trimmed2,ID9_CP_nc_comp)
plt.plot(t_CP_c_trimmed2,ID9_CP_c_comp)
plt.legend()
plt.xlabel('Time (ms)')
plt.ylabel('Angle °')
plt.show()
####################################

TD_ID9_entered_angle_construct = np.arange(562)

TD_ID9_entered_angle_construct[1] = 149

TD_ID9_entered_angle_construct= TD_ID9_entered_angle_construct.astype('float64')
i = 2
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 95 / 40
    i = i + 1
    if i == 40:
        break
TD_ID9_entered_angle_construct[40] = 54
TD_ID9_entered_angle_construct[41] = 54


i = 42
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 84 / 40
    i = i + 1
    if i == 80:
        break
TD_ID9_entered_angle_construct[80] = 138
TD_ID9_entered_angle_construct[81] = 138
i = 82
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 82 /40
    i = i + 1
    if i == 120:
        break
TD_ID9_entered_angle_construct[120] = 56
TD_ID9_entered_angle_construct[121] = 56
i = 122
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 70 / 40
    i = i + 1
    if i == 160:
        break
TD_ID9_entered_angle_construct[160] = 126
TD_ID9_entered_angle_construct[161] = 126
i = 162
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 67 / 40
    i = i + 1
    if i == 200:
        break
TD_ID9_entered_angle_construct[200] = 59
TD_ID9_entered_angle_construct[201] = 59
i = 202
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 56 / 40
    i = i + 1
    if i == 240:
        break
TD_ID9_entered_angle_construct[240] = 115
TD_ID9_entered_angle_construct[241] = 115
i = 242
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 54 / 40
    i = i + 1
    if i == 280:
        break
TD_ID9_entered_angle_construct[280] = 61
TD_ID9_entered_angle_construct[281] = 61
i = 282
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 43 / 40
    i = i + 1
    if i == 320:
        break
TD_ID9_entered_angle_construct[320] = 104
TD_ID9_entered_angle_construct[321] = 104

i = 322
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 41 / 40
    i = i + 1
    if i == 360:
        break
TD_ID9_entered_angle_construct[360] = 63
TD_ID9_entered_angle_construct[361] = 63
i = 362
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 30 / 40
    i = i + 1
    if i == 400:
        break
TD_ID9_entered_angle_construct[400] = 93
TD_ID9_entered_angle_construct[401] = 93
i = 402
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 28 / 40
    i = i + 1
    if i == 440:
        break
TD_ID9_entered_angle_construct[440] = 65
TD_ID9_entered_angle_construct[441] = 65
i = 442
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 16 / 40
    i = i + 1
    if i == 480:
        break
TD_ID9_entered_angle_construct[480] = 81
TD_ID9_entered_angle_construct[481] = 81
i = 482
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] - 13 / 40
    i = i + 1
    if i == 520:
        break
TD_ID9_entered_angle_construct[520] = 68
TD_ID9_entered_angle_construct[521] = 68
i = 522
while TD_ID9_entered_angle_construct[i] < TD_ID9_entered_angle_construct.size:
    TD_ID9_entered_angle_construct[i] = TD_ID9_entered_angle_construct[i - 1] + 2 / 40
    i = i + 1
    if i == 560:
        break
TD_ID9_entered_angle_construct[560] =70
TD_ID9_entered_angle_construct[561] = 70


TD_End_70s_a = 70 * np.ones(89)
TD_End_70s_a = TD_End_70s_a.tolist()
TD_ID9_entered_angle_construct = TD_ID9_entered_angle_construct.tolist()

TD_ID9_entered_angle_construct.pop(0)

TD_ID9_entered_angle_length650 = TD_ID9_entered_angle_construct + TD_End_70s_a

TD_ID9_entered_angle_length646 = TD_ID9_entered_angle_length650[:646]
TD_ID9_entered_angle_length641 = TD_ID9_entered_angle_length650[:641]


#######

CP_ID9_entered_angle_1192element = np.arange(842)

CP_ID9_entered_angle_1192element[1] = 135


i = 2
CP_ID9_entered_angle_1192element=CP_ID9_entered_angle_1192element.astype('float64')
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] - 55 / 105
    i=i+1
    if i == 105:
        break
CP_ID9_entered_angle_1192element[105]=80.5238
CP_ID9_entered_angle_1192element[106] = 80
i = 107
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] + 39 / 105
    i = i + 1
    if i == 210:
        break
CP_ID9_entered_angle_1192element[210] = 1.186285714285709e+02
CP_ID9_entered_angle_1192element[211] = 119
i = 212
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] - 41 / 105
    i = i + 1
    if i == 315:
        break
CP_ID9_entered_angle_1192element[315] = 78.3904761904760
CP_ID9_entered_angle_1192element[316] = 78
i = 317
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] + 25 / 105
    i = i + 1
    if i == 420:
        break
CP_ID9_entered_angle_1192element[420] = 1.027619047619050e+02
CP_ID9_entered_angle_1192element[421] = 103

i = 422
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] - 28 / 105
    i = i + 1
    if i == 525:
        break
CP_ID9_entered_angle_1192element[525] = 75.266666666666770
CP_ID9_entered_angle_1192element[526] = 75


i = 527
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] + 11 / 105
    i = i + 1
    if i == 630:
        break

CP_ID9_entered_angle_1192element[630] = 85.8952380952377
CP_ID9_entered_angle_1192element[631] = 86


i = 632
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] -13 / 105
    i = i + 1
    if i == 735:
        break
CP_ID9_entered_angle_1192element[735] = 73.123809523809200
CP_ID9_entered_angle_1192element[736] = 73
i = 737
while CP_ID9_entered_angle_1192element[i] < CP_ID9_entered_angle_1192element.size:
    CP_ID9_entered_angle_1192element[i] = CP_ID9_entered_angle_1192element[i - 1] -3/ 105
    i = i + 1
    if i == 840:
        break
CP_ID9_entered_angle_1192element[840] = 70.028571428571810
CP_ID9_entered_angle_1192element[841] = 70

CP_End_70s_a = 70*np.ones(351)
CP_End_70s_a = CP_End_70s_a.tolist()

CP_ID9_entered_angle_1192element = CP_ID9_entered_angle_1192element.tolist()
CP_ID9_entered_angle_1192element.pop(0)

CP_ID9_entered_angle_1192element_final = CP_ID9_entered_angle_1192element + CP_End_70s_a
CP_ID9_entered_angle_1192element_final1=CP_ID9_entered_angle_1192element_final

CP_ID9_entered_angle_1192element_final1 = np.array(CP_ID9_entered_angle_1192element_final1)

CP_ID9_entered_angle_length298= np.arange(299)
CP_ID9_entered_angle_length298=CP_ID9_entered_angle_length298.astype(float)
CP_ID9_entered_angle_length298[0] = 135
CP_ID9_entered_angle_length298[1] =135
i = 2
while i <= 298:

    CP_ID9_entered_angle_length298[i] = CP_ID9_entered_angle_1192element_final1[1+4*(i-1)]
    i = i + 1

CP_ID9_entered_angle_length298=CP_ID9_entered_angle_length298.tolist()
CP_ID9_entered_angle_length298.pop(0)
CP_ID9_entered_angle_length296 = CP_ID9_entered_angle_length298[:296]




time_2970_1192entries = np.arange(1192)
time_2970_1192entries = time_2970_1192entries.astype(float)

time_2970_1192entries[1] = 0

i = 1
while i <= 1191:

    time_2970_1192entries[i] = time_2970_1192entries[i-1] + 2.5
    i = i + 1

time_2970_1192entries = time_2970_1192entries.tolist()


from sklearn.metrics import mean_squared_error
from math import sqrt

R_TD_nc_uncomp_matrix = np.corrcoef(ID9_TD_nc_uncomp, TD_ID9_entered_angle_length641)
Rms_TD_nc_uncomp = sqrt(mean_squared_error(ID9_TD_nc_uncomp, TD_ID9_entered_angle_length641))

R_TD_nc_comp_matrix = np.corrcoef(ID9_TD_nc_comp, TD_ID9_entered_angle_length641)
Rms_TD_nc_comp = sqrt(mean_squared_error(ID9_TD_nc_comp, TD_ID9_entered_angle_length641))

R_TD_c_uncomp_matrix = np.corrcoef(ID9_TD_c_uncomp, TD_ID9_entered_angle_length646)
Rms_TD_c_uncomp = sqrt(mean_squared_error(ID9_TD_c_uncomp, TD_ID9_entered_angle_length646))

R_TD_c_comp_matrix = np.corrcoef(ID9_TD_c_comp, TD_ID9_entered_angle_length646)
Rms_TD_c_comp = sqrt(mean_squared_error(ID9_TD_c_comp, TD_ID9_entered_angle_length646))



R_CP_nc_uncomp_matrix = np.corrcoef(ID9_CP_nc_uncomp, CP_ID9_entered_angle_length298)
Rms_CP_nc_uncomp = sqrt(mean_squared_error(ID9_CP_nc_uncomp, CP_ID9_entered_angle_length298))

R_CP_nc_comp_matrix = np.corrcoef(ID9_CP_nc_comp, CP_ID9_entered_angle_length298)
Rms_CP_nc_comp = sqrt(mean_squared_error(ID9_CP_nc_comp, CP_ID9_entered_angle_length298))


R_CP_c_uncomp_matrix = np.corrcoef(ID9_CP_c_uncomp, CP_ID9_entered_angle_length296)
Rms_CP_c_uncomp = sqrt(mean_squared_error(ID9_CP_c_uncomp, CP_ID9_entered_angle_length296))

R_CP_c_comp_matrix = np.corrcoef(ID9_CP_c_comp, CP_ID9_entered_angle_length296)
Rms_CP_c_comp = sqrt(mean_squared_error(ID9_CP_c_comp, CP_ID9_entered_angle_length296))

print(Rms_CP_c_comp)