x = ["apple", "banana", "blueberries", "coconut", "strawberry", "clementine"]
lengths = []

for i in range(len(x)):
    lengths.append(len(x[i]))

lengths.sort()

sortedL = []

print(lengths)

for length in lengths:
    for i in range(len(x)):
        if len(x[i]) == length:
            sortedL.append(x[i])
            x.remove(x[i])
            break

print(sortedL)