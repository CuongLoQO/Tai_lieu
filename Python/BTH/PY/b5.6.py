def fibo(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
n=int(input("N = "))
F=[k for k in fibo(n)]
print(F)
    
