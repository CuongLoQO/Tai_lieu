#Bài 3
def kc(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def area(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
def area2(x1,y1,x2,y2,x3,y3):
    a=kc(x1,y1,x2,y2)
    b=kc(x2,y2,x3,y3)
    c=kc(x3,y3,x1,y1)
    p=(a+b+c)/2
    dt=area(a,b,c)
    return dt
print(area2(1,3,2,4,2,5))

