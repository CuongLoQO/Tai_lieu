d = 0
n=int(input("N = "))
for i in range(2,n+1,2):
    d=d+i**2
print("P("+str(n)+") =",d)
