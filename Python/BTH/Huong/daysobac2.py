N = int(input("N = "))

sum = 0
T = 0

for i in range (1, N + 1):
    T += i**2 
    sum += N / T
    
print("F(%d) = %.7f" %(N, sum))