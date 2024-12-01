
import math

N = int(input("N = "))

sum = 0
t = 0
for i in range (1, N + 1):
    t += i
    sum += i/t
    
print("F("+str(N)+") =",'{:.7f}'.format(sum))
