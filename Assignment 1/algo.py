S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Sp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 's']

f = True
inc = 0

for i in range(len(S)):
    if S[i] == Sp[inc]:
        if inc < len(Sp):
            inc += 1
        if inc == len(Sp):
            f = False
            print('true')
            break
    else:
        inc = 0

if f:
    print('false')
