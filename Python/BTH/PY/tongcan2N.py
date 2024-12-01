import math
n=int(input("N = "))
a=0
s=0
for i in range(1,n+1):
    a=a+i
    s=s+math.sqrt(a)
print("F("+str(n)+") =",round(s,7))
