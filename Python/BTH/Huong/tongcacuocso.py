N = int(input("N = "))

sum = 0
for i in range(1, int(N**(1/2) + 1)):
     if N % i == 0:
         sum += i
         j = N // i
         if j != i:
            sum += j

print("Tong cac uoc so cua %d la %d" %(N, sum))