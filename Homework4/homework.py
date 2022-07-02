# EXERCISE 4.1
# -----------------------------------------------
print('Exercise 4.1')
print('------------')

x = 1.2
y = -0.87
in_circle = lambda x, y : x**2 + y**2
if in_circle(x,y) < 1:
    print('(a) p(x,y) is in unit circle')
else:
    print('(a) p(x,y) is not in unit circle')


test_positive = lambda x, y : x>0 and y>0
if test_positive(x,y):
    print('(b) coordinates of p are positive')
else:
    print('(b) coordinates of p are not positive')


# EXERCISE 4.2
# -----------------------------------------------
print('Exercise 4.2')
print('------------')

L = [0,1,2,3,4,5,6,7,8,9]
print('Original list: {}'.format(L))
def reverse_range(list,i,j):
    l = []
    for k in range(i,j+1):
        l.insert(0,L[k])
    n = 0
    for k in range(i,j+1):
        L[k] = l[n]
        n+=1

reverse_range(L,3,6)
print('Reversed list from index 3 to 6: {}'.format(L))

# EXERCISE 4.3
# -----------------------------------------------
print('Exercise 4.3')
print('------------')

def iter_even():
    i = 0
    while True:
        yield 2*i
        i+=1
        
print(iter_even())

def iter_odd():
    i = 0
    yield 2*i+1
    i+=1

print(iter_odd())

k = 2
def iter_power(k):
    i = 0
    while True:
        yield k**i
        i+=1

print(iter_power(k))
