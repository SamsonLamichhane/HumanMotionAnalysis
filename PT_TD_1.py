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

read_file = pd.read_excel('PT_TD_1.xlsx')
df = pd.read_excel('PT_TD_1.xlsx')


df["Time (ms)"] = pd.to_numeric(df["Time (ms)"], downcast="float")
df["x-axis acceleration"] = pd.to_numeric(df["x-axis acceleration"], downcast="float")
df["x-axis acceleration"] = ((df["x-axis acceleration"] * 9.81) / 8192)

df["y-axis acceleration"] = pd.to_numeric(df["y-axis acceleration"], downcast="float")
df["y-axis acceleration"] = ((df["y-axis acceleration"] * 9.81) / 8192)

df["z-axis acceleration"] = pd.to_numeric(df["z-axis acceleration"], downcast="float")
df["z-axis acceleration"] = ((df["z-axis acceleration"] * 9.81) / 8192)


xGyroOffset = 0.726998645
yGyroOffset = -0.953258808
zGyroOffset = 0.666212737

df["x-axis gyroscope"] = pd.to_numeric(df["x-axis gyroscope"], downcast="float")
df["x-axis gyroscope"] = (df["x-axis gyroscope"] / 16.4)

df["y-axis gyroscope"] = pd.to_numeric(df["y-axis gyroscope"], downcast="float")
df["y-axis gyroscope"] = (df["y-axis gyroscope"] / 16.4)

df["z-axis gyroscope"] = pd.to_numeric(df["z-axis gyroscope"], downcast="float")
df["z-axis gyroscope"] = (df["z-axis gyroscope"] / 16.4)

df['gx_TD_uncomp']=df["x-axis gyroscope"]
df['gy_TD_uncomp']=df["y-axis gyroscope"]
df['gz_TD_uncomp']=df["z-axis gyroscope"]
gx_TD_uncomp=df['gx_TD_uncomp'].tolist()
gy_TD_uncomp=df['gy_TD_uncomp'].tolist()
gz_TD_uncomp=df['gz_TD_uncomp'].tolist()

df['gx_TD_comp']=df["x-axis gyroscope"] - xGyroOffset
df['gy_TD_comp']=df["y-axis gyroscope"] - yGyroOffset
df['gz_TD_comp']=df["z-axis gyroscope"] - zGyroOffset

gx_TD_comp_int  = integrate.cumtrapz(df['gx_TD_comp'], dx=0.01)
gy_TD_comp_int  = integrate.cumtrapz(df['gy_TD_comp'], dx=0.01)
gz_TD_comp_int  = integrate.cumtrapz(df['gz_TD_comp'], dx=0.01)

gx_TD_comp=df['gx_TD_comp'].tolist()
gy_TD_comp=df['gy_TD_comp'].tolist()
gz_TD_comp=df['gz_TD_comp'].tolist()


gx_TD_comp_int=gx_TD_comp_int.tolist()
gy_TD_comp_int = gy_TD_comp_int.tolist()
gz_TD_comp_int = gz_TD_comp_int.tolist()

gx_TD_comp_int.insert(0,0)
gy_TD_comp_int.insert(0,0)
gz_TD_comp_int.insert(0,0)

t1 = [a * b for a, b in zip(gx_TD_comp_int, gx_TD_comp_int)]
t2 = [a * b for a, b in zip(gy_TD_comp_int, gy_TD_comp_int)]
t3 = [a * b for a, b in zip(gz_TD_comp_int, gz_TD_comp_int)]

total = []

for i in range(0, len(t1)):
    total.append(t1[i] + t2[i]+ t3[i])

total = np.array(total)

vector_TD_comp = np.sqrt(total)
vector_TD_comp_ID9 = vector_TD_comp*-1 + 149
vector_TD_comp = vector_TD_comp.tolist()
vector_TD_comp_ID9=vector_TD_comp_ID9.tolist()
t_D=np.arange(0,9991,10)
t_D=t_D.tolist()

ax3 = plt.gca()
plt.plot(t_D,gx_TD_comp,label='X-axis')
plt.plot(t_D,gy_TD_comp,label='Y-axis')
plt.plot(t_D,gz_TD_comp,label='Z-axis')
plt.legend()
plt.show()

ax4 = plt.gca()
plt.plot(t_D,gx_TD_comp_int,label='X-axis')
plt.plot(t_D,gy_TD_comp_int,label='Y-axis')
plt.plot(t_D,gz_TD_comp_int,label='Z-axis')
plt.legend()
plt.show()

ax5 = plt.gca()
plt.plot(t_D,gx_TD_comp_int,label='X-axis')
plt.plot(t_D,gy_TD_comp_int,label='Y-axis')
plt.plot(t_D,gz_TD_comp_int,label='Z-axis')
plt.plot(t_D,vector_TD_comp,label='Vector')
plt.legend()
plt.show()


metric_EX = max(vector_TD_comp)
metric_FA = metric_EX
metric_SA = 0

metric_RA = vector_TD_comp[-1]

metric_RI = (metric_SA - metric_FA)/(metric_SA - metric_RA)

start_time = 1100
end_time = 10000
metric_t = (end_time - start_time)/1000