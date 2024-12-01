ho=set()
ten=set()
while 1:
    a=input("Nhap: ").split()
    if len(a)==0: break
    ho.add(a[0])
    ten.add(a[-1])
print(ho,"\n")
print(ten)
