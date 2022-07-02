# EXERCISE 3.1
# -----------------------------------------------
print('Exercise 3.1')
print('------------')

word = 'Pratixan'
line = '+---'
endline = '+---+'
N = len(word)
for i in range(N):
    if i == N-1:
        print(endline)
    else:
        print(line,end='')

#print('\n')
for j in range(N): 
    if j == N-1:
        print('| {} |'.format(word[j]))
    else:
        print('| {} '.format(word[j]),end='')

for i in range(N):
    if i == N-1:
        print(endline)
    else:
        print(line,end='')

        
# EXERCISE 3.2
# -----------------------------------------------
print('Exercise 3.2')
print('------------')

print('Using For loop:\n')
for x in range(1,41):
    #print(x)
    if x % 5 == 0 and x % 7 == 0:
        print('x is divided by 5 and 7')
    elif (x % 5 == 0):
        print('x is divided by 5')
    elif (x % 7 == 0):
        print('x is divided by 7')
    elif x == 13:
        continue
    elif x % 5 != 0 and x % 7 != 0:
        print('x is not important')

print('\nUsing While loop:\n')
x = 1
while x <= 40:
    #print(x)
    if x % 5 == 0 and x % 7 == 0:
        print('x is divided by 5 and 7')
    elif (x % 5 == 0):
        print('x is divided by 5')
    elif (x % 7 == 0):
        print('x is divided by 7')
    elif x == 13:
        pass
    elif x % 5 != 0 and x % 7 != 0:
        print('x is not important')

    x+=1
        
# EXERCISE 3.3
# -----------------------------------------------
print('Exercise 3.3')
print('------------')

import math
n = 2022
x = math.pi

print('n = {}'.format(n))
print('pi = {:.5f}'.format(x))
word = "Python"
polish = "ksiazka"

with open('vars.txt', 'w') as file:
    file.write('{}\n{}\n'.format(word,polish))
    
with open('vars.txt', 'r') as file:
    print(file.read())
