N = int(input("N = "))
s, f = 0, 0
for i in range(1,N+1):
        s+=i
        f = f+ s**(1/i)
print("F("+str(N)+") =",'{:.7f}'.format(f))
