n = int(input("Nhap N duong: "))

sum = 0

giaithua = 1

for i in range(1,n+1):
    giaithua = giaithua*i
    sum += giaithua

print("F(%d) = %d" %(n, sum))