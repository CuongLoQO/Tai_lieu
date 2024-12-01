def isprime(n):
    x=2
    while x<n:
        if(n%x==0):
            return False
            break
        x=x+1
    else : return True
a=int(input("Nhập A: "))
b=int(input("Nhập B: "))
for i in range(a,b+1):
    if isprime(i)==True:
        print(i,end=' ')
