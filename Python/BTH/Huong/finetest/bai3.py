n = int(input("Nhap N: "))
A = []
B = []
for i in range(1, n+1):
    k = input("Nhap gia tri thu "+str(i)+": ")
    try:
        A.append(float(k))
    except:
        b.append((k))
s = 0
for w in A:
    s += w
print("Tong cac phan tu cua A =", s)
print(f"B = {sorted(B, reverse = True)}")
