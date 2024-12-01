n = int(input("N = "))

if n % 2 == 1 :
    print("N khong phai la so fibonacci chan")
    exit()
a = 0
b = 1
while True:
    c = a + b
    a = b
    b = c
    if a == n:
        print("N la so fibonacci chan")
        break
    if a > n:
        print("N khong phai la so fibonacci chan")
        break
