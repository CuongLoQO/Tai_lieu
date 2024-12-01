def kt(s):
	s = s.replace(".", "", 1)
	if s[0] == '-': s = s.replace("-", "", 1)
	if s.isdigit():
		return True
	return False

n = int(input("Nhap N: "))
A, B, C = [], [], []

for i in range (1, n + 1):
	s = input("Nhap gia tri thu %d: " %i)
	if s.isdigit() or (s[0] == "-" and s[1:].isdigit()):
		A.append(int(s))
	elif kt(s):
		B.append(float(s))
	else:
		C.append(s)
		
A.sort(reverse = True)
B.sort(reverse = True)
C.sort(reverse = True)

print("A =", A)
print("B =", B)
print("C =", C)