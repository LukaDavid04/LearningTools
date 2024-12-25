x = [10, 9, 18, 115, 1114, 11113, 111112, 111111111]
last = 0
seq = 0
highseq = 0

for i in range(len(x)):
    index = x[i]
    if x[i] > last:
        seq = seq + 1
        if seq >= highseq:
            highseq = seq
    else:
        seq = 1
    last = x[i]

print(highseq)