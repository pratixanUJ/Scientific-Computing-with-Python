import numpy as np

# EXERCISE 2.1
# -----------------------------------------------
print('Exercise 2.1')
print('------------')

n = 100101001
print('Long positive integer: n = {}'.format(n))
#counting the number of zeros
count = str(n).count('0')
print('Number of zeroes in n = {}'.format(count))

# EXERCISE 2.2
# -----------------------------------------------
print('\nExercise 2.2')
print('------------')

x = 5
print('x == 5 and 3 : {}  # The left operand is True which is why it returns the right operand'.format(x == 5 and 3))
print('x == 4 and 3 : {}  # The left operand is False which is why it returns False i.e the left operand'.format(x == 4 and 3))
print('3 and x == 5 : {}  # The left operand is True which is why it returns the right operand which is True'.format(3 and x == 5))
print('3 and x == 4 : {}  # The left operand is True which is why it returns the right operand which is False'.format(3 and x == 4))

print('')
print('isinstance(True, int) : {}'.format(isinstance(True, int)))
print('isinstance(True, int) : {}'.format(isinstance(True, bool)))
print('# Explanation - The "True" in python is both associated to type int (i.e True = 1) and type bool,')
print('# hence both of the above function returned True')


# EXERCISE 2.3
# -----------------------------------------------
print('\nExercise 2.3')
print('------------')

Sum = 0
for i in range(1011):
    Sum += (2*i+1)*(2*i+1)
    
print('The sum of 1*1 + 3*3 + 5*5 + ... + 2021*2021 is {}'.format(Sum))

# EXERCISE 2.4
# -----------------------------------------------
print('\nExercise 2.4')
print('------------')
print('(a)')
i = 0
list = []
name = 'Pratixan'
for i in range(len(name)):
    list.append(ord(name[i]))
    i+=1
    
print('Pratixan --> {}'.format(list))

print('\n(b)')
from tabulate import tabulate 
pt = [(1,"Hydrogen","H",1),(2,"Helium","He",4),(3,"Lithium","Li",7),(4,"Berylium","Be",9),(5,"Boron","B",11),(6,"Carbon","C",12),(7,"Nitrogen","N",14),(8,"Oxygen","O",16),(9,"Fluorine","F",19),(10,"Neon","Ne",20)]
header = ["No.","Name (en)","Symbol","Weight (u)"]
print(tabulate(pt,header,tablefmt="pretty"))

# EXERCISE 2.5
# -----------------------------------------------
print('\nExercise 2.5')
print('------------')

# EXERCISE 2.6
# -----------------------------------------------
print('\nExercise 2.6')
print('------------')

t = (2,4)
print('print(t[2]) returns error: tuple out of range')
print('t.append(6) return error: tuple has no attribute append()')
a, b = t ; print(a, b) #returns the elements of the tuple

# EXERCISE 2.7
# -----------------------------------------------
print('\nExercise 2.7')
print('------------')

D = {}
i=0
for r in ['I','IV','V','IX','X','XL','XC','C','CD','D','CM','M']:
    nums = [1,4,5,9,10,40,90,100,400,500,900,1000]
    D[r] = nums[i]
    i += 1

print(D)
