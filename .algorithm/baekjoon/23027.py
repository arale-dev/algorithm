S = input()
res = list(S)
if 'A' in S:
    for i in range(len(S)):
        s = S[i]
        if s == 'B' or s == 'C' or s == 'D' or s == 'F':
            res[i] = 'A'
elif 'B' in S:
    for i in range(len(S)):
        s = S[i]
        if s == 'C' or s == 'D' or s == 'F':
            res[i] = 'B'
elif 'C' in S:
    for i in range(len(S)):
        s = S[i]
        if s == 'D' or s == 'F':
            res[i] = 'C'
else:
    res = 'A' * len(S)

print("".join(res))