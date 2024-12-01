def nhap(tb1,tb2):
    dic ={}
    print(tb1)
    while True:
        name=input("  Ten mat hang: ")
        if len(name) == 0: break
        dic[name]= float(input(f'  {tb2}'))
    return dic
a=nhap("NHAP BANG GIA:","Gia ban hang: ")
b=nhap("NHAP HANG TON:","So luong ton kho: ")
L={i: a[i]*b[i] if i in b else 0 for i in a}
L=dict(sorted(L.items(),key=lambda x: x))
L=dict(sorted(L.items(),key=lambda x: x[1],reverse=True))
print("THONG KE HANG TON:")
for i,j in L.items():
    print("  "+i.ljust(max([len(x) for x in L])) +" " + "{:.2f}".format(j).rjust(6))

