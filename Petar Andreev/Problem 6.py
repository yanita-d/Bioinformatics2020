
s = 'GATATATGCATATACTT'
t = 'ATAT'
result = []
slen = len(s)
tlen = len(t)

for i in range(slen - tlen):
    if s[i:i+tlen] == t:
        result.append(i+1)

print(result)