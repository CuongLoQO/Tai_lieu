def isPrime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
n = int(input("Nhập N: "))
print(isPrime(n))
