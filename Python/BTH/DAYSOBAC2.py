s=0
d=0
n=int(input("N = "))
for i  in range(1,n+1):
    s+=i*i
    d+=n/s
print("F("+str(n)+") = %.7f" %d)
