import random

x = []

for i in range(5):
    x.append(random.randint(1, 10))

smallest = x[0]

for j in range(len(x)):
    if x[j] < smallest:
        smallest = x[j]

print(x, smallest)
if smallest == min(x):
    print("Test Passed")
else:
    print("Test Failed")