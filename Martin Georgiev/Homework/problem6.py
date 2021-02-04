def findLocations(s, t):
    result = []
    for idx in range(0, len(s) - len(t) + 1):
        if(s[idx : idx+len(t)] == t):
            result.append(idx + 1)

    print(result)

#findLocations('GATATATGCATATACTT', 'ATAT')
#2 4 10
#findLocations('AAAAA', 'A')
#1 2 3 4 5
#findLocations('MAMAMA', 'MA')
#1 3 5
#findLocations('PESHO', 'PESHO')
#1
