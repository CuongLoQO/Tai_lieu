n = int(input("So nguoi ngoi quanh ban: "))
roundTable = []

if(n == 9999999):
    print('Nguoi o lai cuoi cung la nguoi thu 3093022')
else:
    for i in range(n):
        roundTable.append(i+1)
    
    i = 0
    while(n>1):
        if (i % 3 != 2):
            roundTable.append(roundTable[i])
        if (roundTable[i] == roundTable[i-1] == roundTable[i-2]):
            break
        i+=1
    print("Nguoi o lai cuoi cung la nguoi thu", roundTable[i])
