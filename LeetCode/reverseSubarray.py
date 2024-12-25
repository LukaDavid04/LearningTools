x = [1, 2, 3, 4, 5, 6, 7]
start = 0
end = 3

ans = []

for i in range(0, start):
    ans.append(x[i])
for i in range(end, start - 1, -1):
    ans.append(x[i])
for i in range(end + 1, len(x)):
    ans.append(x[i])

print(ans)