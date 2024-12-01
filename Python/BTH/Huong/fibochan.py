import math

N = int(input("N = "))

def Square(x):
	s = int(math.sqrt(x))
	return s * s == x

def Fibonacci(m):
	return Square(5 * m * m + 4) or Square(5 * m * m - 4)
	

if (Fibonacci(N) == True and N % 2 == 0):
	print ("N la so fibonacci chan")
else:
	print ("N khong phai la so fibonacci chan")
