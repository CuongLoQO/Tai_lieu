s, d=0, 0
n = int(input("N = "))
if n%2==0:
    for i in range(2, n+1, 2):
        s=i**2
        d+=s
print("P(", n, ") = ", d, sep='')
