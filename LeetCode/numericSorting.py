x = ["xpple", "banana", "xpple", "orange", "banana", "banana", "orange", "z", "z", "y", "y"]
xdict = {}

for i in range(len(x)):
    if x[i] in xdict:
        xdict[x[i]] = xdict[x[i]] + 1
    else:
        xdict[x[i]] = 1


sd = dict(sorted(xdict.items()))
sd2 = dict(sorted(sd.items(), key=lambda item: item[1], reverse = True))


print(list(sd2.keys()))
