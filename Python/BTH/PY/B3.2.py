def isPrime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
a = int(input("Nhập A: "))
b = int(input("Nhập B: "))

for i in range(a,b+1):
    if isPrime(i)==True:
        print(i, end=" ")
        
