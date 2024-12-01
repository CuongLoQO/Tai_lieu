s, d=0, 0
n = int(input("N = "))
if n>0:
    for i in range(1, n+1):
        s=i**2
        d+=s
print("P(", n, ") = ", d, sep='')
