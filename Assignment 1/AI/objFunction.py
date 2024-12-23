import math
import random
b = 1
c = 100
r = random.random()

# candidate - intial
# if positive candidate is better
x = math.exp(((-b/c))/0.9)
y = math.exp(((-b/c))/0.7)
z = math.exp(((-b/c))/0.5)
f = math.exp(((-b/c))/0.3)
g = math.exp(((-b/c))/0.1)


print(x, y, z, f, g)
print(r)
print(r < x)
