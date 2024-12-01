def next_line(L):
    return [1] + [L[i-1]+L[i] for i in range(1,len(L))] + [1]
    
n = int(input("N = "))
L = [1]
for i in range(n):
    print(L)
    L=next_line(L)
