x = [1, 2, 4, 5, 9, 2, 1, 10, 11, 1]
y = [1, 2]
ctr = 0
occur = 1

for i in range(len(x)):
    if x[i] == 1:
        ctr = ctr + 1

print(ctr)

ctrs = []

# count multiple
for i in range(len(y)):
    ctrs.append(0)

for i in range(len(x)):
    for j in range(len(y)):
        if x[i] == y[j]:
            ctrs[j] = ctrs[j] + 1

print(ctrs)