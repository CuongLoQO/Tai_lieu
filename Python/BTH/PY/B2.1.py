import math
#Bài 1
def average(a,b,c,d,e):
    tbc = (a+b+c+d+e)/5
    return tbc
print(average(1,2,3,4,5))
#Bài 2
def area(a,b,c):
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
print(area(3,4,5))
#Bài 3
def area2(x1,y1,x2,y2,x3,y3):
    a=(((x2-x1)**2) + ((y2-y1)**2))**0.5
    b=(((x3-x2)**2) + ((y3-y2)**2))**0.5
    c=(((x1-x3)**2) + ((y1-y3)**2))**0.5
    p=(a+b+c)/2
    s=area(a,b,c)
    return s
print(area2(1,1,2,2,3,3))
#Bài 4
def total(n):
    t=0
    while (n>0):
        t=t+n%10
        n=n//10
    return t
print(total(123))
#Bài 5
def isFibo(n)
    f0=0
    f1=1
    fn=1
    if n < 0:
        return True
    elif n==0||n==1:
        
