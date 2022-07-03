# EXERCISE 10.2
# -----------------------------------------------
print('Exercise 10.2')
print('------------')

import pandas as pd

temp = [30,32,27]
s1 = pd.Series(temp,name='Temperatures at noon (Celcius)')
s1.index = ['01/07/2022','02/07/2022','03/07/2022']

print(s1)

# EXERCISE 10.3
# -----------------------------------------------
print('Exercise 10.3')
print('------------')

D = [{'Name':"Hydrogen",'Symbol':'H','Weight(u)':1},{'Name':"Helium",'Symbol':'He','Weight(u)':4},{'Name':"Lithium",'Symbol':'Li','Weight(u)':7},{'Name':"Berylium",'Symbol':'Be','Weight(u)':9},{'Name':"Boron",'Symbol':'B','Weight(u)':11},{'Name':"Carbon",'Symbol':'C','Weight(u)':12},{'Name':"Nitrogen",'Symbol':'N','Weight(u)':14},{'Name':"Oxygen",'Symbol':'O','Weight(u)':16},{'Name':"Fluorine",'Symbol':'F','Weight(u)':19},{'Name':"Neon",'Symbol':'Ne','Weight(u)':20}]
s2 = pd.DataFrame(D,index=[i for i in range(1,11,1)])
print(s2)

