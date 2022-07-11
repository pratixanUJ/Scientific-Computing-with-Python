# EXERCISE 10.1
# -----------------------------------------------
#pratixan@LAPTOP-7DHV6106:~$ sudo apt install python3-venv
#pratixan@LAPTOP-7DHV6106:~$ python3 -m venv VE1
#pratixan@LAPTOP-7DHV6106:~$ ls
#pratixan@LAPTOP-7DHV6106:~$ ls VE1/
#bin  include  lib  lib64  pyvenv.cfg  share
#pratixan@LAPTOP-7DHV6106:~$ cat VE1/pyvenv.cfg
#home = /usr/bin
#include-system-site-packages = false
#version = 3.8.10
#
#pratixan@LAPTOP-7DHV6106:~$ source VE1/bin/activate
#(VE1) pratixan@LAPTOP-7DHV6106:~$ pip list
#Package       Version
#------------- -------
#pip           20.0.2
#pkg-resources 0.0.0
#setuptools    44.0.0
#
#(VE1) pratixan@LAPTOP-7DHV6106:~$ pip install numpy
#Collecting numpy
#  Downloading numpy-1.23.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.1 MB)
#     |████████████████████████████████| 17.1 MB 338 kB/s
#Installing collected packages: numpy
#Successfully installed numpy-1.23.1
#
#(VE1) pratixan@LAPTOP-7DHV6106:~$ pip install matplotlib
#Collecting matplotlib
#  Downloading matplotlib-3.5.2-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (11.3 MB)
#     |████████████████████████████████| 11.3 MB 4.6 MB/s
#Collecting pillow>=6.2.0
#  Downloading Pillow-9.2.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
#     |████████████████████████████████| 3.1 MB 227 kB/s
#Requirement already satisfied: numpy>=1.17 in ./VE1/lib/python3.8/site-packages (from matplotlib) (1.23.1)
#Collecting pyparsing>=2.2.1
#  Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)
#     |████████████████████████████████| 98 kB 276 kB/s
#Collecting kiwisolver>=1.0.1
#  Downloading kiwisolver-1.4.3-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.2 MB)
#     |████████████████████████████████| 1.2 MB 1.8 MB/s
#Collecting packaging>=20.0
#  Downloading packaging-21.3-py3-none-any.whl (40 kB)
#     |████████████████████████████████| 40 kB 1.0 MB/s
#3Collecting cycler>=0.10
#  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
#Collecting fonttools>=4.22.0
#  Downloading fonttools-4.34.4-py3-none-any.whl (944 kB)
#     |████████████████████████████████| 944 kB 404 kB/s
#Collecting python-dateutil>=2.7
#  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
#     |████████████████████████████████| 247 kB 2.0 MB/s
#Collecting six>=1.5
#  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
#Installing collected packages: pillow, pyparsing, kiwisolver, packaging, cycler, fonttools, six, python-dateutil, matplotlib
#Successfully installed cycler-0.11.0 fonttools-4.34.4 kiwisolver-1.4.3 matplotlib-3.5.2 packaging-21.3 pillow-9.2.0 pyparsing-3.0.9 python-dateutil-2.8.
#2 six-1.16.0
#
#(VE1) pratixan@LAPTOP-7DHV6106:~$ pip install pandas
#Collecting pandas
#  Downloading pandas-1.4.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
#     |████████████████████████████████| 11.7 MB 1.9 MB/s
#Requirement already satisfied: python-dateutil>=2.8.1 in ./VE1/lib/python3.8/site-packages (from pandas) (2.8.2)
#Collecting pytz>=2020.1
#  Downloading pytz-2022.1-py2.py3-none-any.whl (503 kB)
#     |████████████████████████████████| 503 kB 2.0 MB/s
#Requirement already satisfied: numpy>=1.18.5; platform_machine != "aarch64" and platform_machine != "arm64" and python_version < "3.10" in ./VE1/lib/python3.8/site-packages (from pandas) (1.23.1)
#Requirement already satisfied: six>=1.5 in ./VE1/lib/python3.8/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)
#Installing collected packages: pytz, pandas
#Successfully installed pandas-1.4.3 pytz-2022.1
#
#(VE1) pratixan@LAPTOP-7DHV6106:~$ pip list
#Package         Version
#--------------- -------
#cycler          0.11.0
#fonttools       4.34.4
#kiwisolver      1.4.3
#matplotlib      3.5.2
#numpy           1.23.1
#packaging       21.3
#pandas          1.4.3
#Pillow          9.2.0
#pip             20.0.2
#pkg-resources   0.0.0
#pyparsing       3.0.9
#python-dateutil 2.8.2
#pytz            2022.1
#setuptools      44.0.0
#six             1.16.0')


# EXERCISE 10.2
# -----------------------------------------------
print('Exercise 10.2')
print('------------')

import pandas as pd
import datetime

temp = [30,32,27,24,25,21,19,18,15,14,13]
dates = pd.date_range("20220701",periods=11)
s1 = pd.Series(temp,name='Temperatures at noon (Celcius)',index=dates)

print(s1)

# EXERCISE 10.3
# -----------------------------------------------
print('Exercise 10.3')
print('------------')

D = [{'Name':"Hydrogen",'Symbol':'H','Weight(u)':1},{'Name':"Helium",'Symbol':'He','Weight(u)':4},{'Name':"Lithium",'Symbol':'Li','Weight(u)':7},{'Name':"Berylium",'Symbol':'Be','Weight(u)':9},{'Name':"Boron",'Symbol':'B','Weight(u)':11},{'Name':"Carbon",'Symbol':'C','Weight(u)':12},{'Name':"Nitrogen",'Symbol':'N','Weight(u)':14},{'Name':"Oxygen",'Symbol':'O','Weight(u)':16},{'Name':"Fluorine",'Symbol':'F','Weight(u)':19},{'Name':"Neon",'Symbol':'Ne','Weight(u)':20}]
s2 = pd.DataFrame(D,index=range(1,11,1))
print(s2)

