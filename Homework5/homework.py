# EXERCISE 5.1
# -----------------------------------------------
print('Exercise 5.1')
print('------------')


import os
import sys

path = '/home/pratixan/win-home/user/Downloads'

def find_pdf_size(top): 
    for filename in os.listdir(top):      #iterating through the directory
        base = filename        
        full_path = os.path.join(top, base)
        if os.path.splitext(base)[1] == '.pdf':
            print('File: {}\nSize: {} Bytes\n'.format(base,os.path.getsize(full_path)))

find_pdf_size(path)


# EXERCISE 5.2
# -----------------------------------------------
print('Exercise 5.2')
print('------------')

import datetime as dt
import numpy as np
date1 = '2021-12-03'
date2 = '2022-05-21'

def print_working_days(date1,date2):
    start = dt.date.fromisoformat(date1)
    end = dt.date.fromisoformat(date2)
    delta = np.busday_count(start,end)
    return delta

days = print_working_days(date1,date2)
print('No of working days from {} to {}: {}'.format(date1,date2,days))


# EXERCISE 5.3
# -----------------------------------------------
print('Exercise 5.3')
print('------------')

import random

def random_walk(start):
    x = start
    directions = ["LEFT","RIGHT"]
    for i in range(100):
        step = random.choice(directions)
        if step == "LEFT":
            x-=1
        elif step == "RIGHT":
            x+=1

    return x

print('Final positon: x = {}'.format(random_walk(0)))
