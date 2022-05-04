import math

x = [60,61,65,63,98,99,90,95,91,96]

n = len(x)

sum = 0

for i in x:
    sum = sum + i

mean = sum/n

squaredList = []

for i in x:
    m = int(i) - mean 
    m = m**2
    squaredList.append(m)

sum = 0
for i in squaredList :
    sum = sum + i

b = n-1
a = sum/b

stdev = math.sqrt(a)

print(stdev)







