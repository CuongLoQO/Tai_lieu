print("NHAP BANG GIA:")
a, b, c = [], [], []
s1 = input("  Ten mat hang: ")
if s1 != "":
    a.append(s1)
    s2 = float(input("  Gia ban hang: "))
    b.append(s2)
while s1 != "":
    s1 = input("  Ten mat hang: ")
    if s1 != "":
        a.append(s1)
        s2 = float(input("  Gia ban hang: "))
        b.append(s2)
    else:
        break
for i in range(len(a)):
    c.append(0)
print("NHAP HANG TON:")
s1 = input("  Ten mat hang: ")
if s1 != "":
    s2 = int(input("  So luong ton kho: "))
    c.pop(a.index(s1))
    c.insert(a.index(s1), s2)
while s1 != "":
    s1 = input("  Ten mat hang: ")
    if s1 != "":
        s2 = int(input("  So luong ton kho: "))
        c.pop(a.index(s1))
        c.insert(a.index(s1), s2)
    else:
        break
maxLen = len(max(a, key=len))
print("THONG KE HANG TON:")
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if b[i] * c[i] < b[j] * c[j]:
            a[i],a[j]=a[j],a[i]
            b[i],b[j]=b[j],b[i]
            c[i],c[j]=c[j],c[i]
        elif b[i] * c[i] == b[j] * c[j]:
            if a[i] > a[j]:
                a[i],a[j]=a[j],a[i]
                b[i],b[j]=b[j],b[i]
                c[i],c[j]=c[j],c[i]
for i in range(len(a)):
    f = round(b[i] * c[i],2)
    while len(a[i]) <= maxLen+3-len(str(f)):
        a[i] += ' '
    print(" ", a[i], end='  ')
    print(f'{f:.2f}')