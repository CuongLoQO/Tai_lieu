import math

N = int(input("N = "))

sum = 0
t = 0
for i in range (1, N + 1):
    sum += math.sqrt(t + i)
    t += i
    
print("F(%d) = %.7f" %(N, sum))