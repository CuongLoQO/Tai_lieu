import math
def dt(a,b,c):
    cv = a + b + c
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p -c))
    return s
a=int(input("Do dai A = "))
b=int(input("Do dai B = "))
c=int(input("Do dai C = "))
d=int(input("Do dai D = "))
s1,s2,s3,s4=0,0,0,0
if (a + b > c) and (a + c > b) and (b + c > a) and a>0 and b>0 and c>0:
    s1=dt(a,b,c)
if (a + b > d) and (a + d > b) and (b + d > a) and a>0 and b>0 and d>0:
    s2=dt(a,b,d)
if (a + d > c) and (a + c > d) and (d + c > a) and a>0 and d>0 and c>0:
    s3=dt(a,d,c)
if (d + b > c) and (d + c > b) and (b + c > d) and d>0 and b>0 and c>0:
    s4=dt(d,b,c)
a=s1+s2+s3+s4
if a==0:
    print("Ket qua = -1")
else :
    print(f'Ket qua = {a:0.5f}')
