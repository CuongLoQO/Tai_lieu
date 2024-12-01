n = int(input("Nhap N: "))
a=[]
b=[]
c=[]
for i in range(1,n+1):
    k=input("Nhap gia tri thu "+str(i)+": ")
    try:
        a.append(int(k))
    except:
        try:
            b.append(float(k))
        except:
            c.append(k)
print(f"A = {sorted(a,reverse=True)}")
print(f"B = {sorted(b,reverse=True)}")
print(f"C = {sorted(c,reverse=True)}")
