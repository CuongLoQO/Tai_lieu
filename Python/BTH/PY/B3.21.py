def isPrime(n):
    x=2
    while x<n:
        if n%x==0:
            return False
            break
        x=x+1
    else: return True
a=int(input("Nhập A: "))
b=int(input("Nhập B: "))
print("Các số nguyên tố từ ",a,"đến ",b," : ")
for i in range(a,b+1):
    if isPrime(i)==True:
        print(i,end=' ')
