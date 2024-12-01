n=int(input("nhap N: "))
d=set()
for i in range(1,n):
    if(n%i==0):
        d.add(i)
for e in d:
    print(e)
