def kt(s):
	s = s.replace(".", "", 1)
	if s[0] == '-': s = s.replace("-", "", 1)
	if s.isdigit():
		return True
	return False

n = int(input("Nhap N: "))

A, B = [], []
tbc = 0
count = 0
for i in range (1, n + 1):
	s = input("Nhap gia tri thu %d: " %i)
	if (s.isdigit() or (s[0] == "-" and s[1:].isdigit())) or kt(s):		
		A.append(float(s))
	else:
		B.append(s)

for i in A:
    count += 1
    tbc += i

if count != 0:
    print("TBC cua A =", tbc / count)
    print("B =", B)
else:
    print("B =", B)