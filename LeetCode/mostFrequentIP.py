f = open("data/IPlogs.txt", "r")
IPs = []
IPf = []

for line in f:
    if line not in IPs:
        IPs.append(line)
        IPf.append(1)
    else:
        IPf[IPs.index(line)] = IPf[IPs.index(line)] + 1

max = 0
maxLine = ''
for line in IPf:
    if line > max:
        max = line
        maxLine = IPs[IPf.index(line)]

print(IPs)
print(IPf)
print(maxLine)