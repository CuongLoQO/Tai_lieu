def Special(y):
    return (y%400==0) or (y%4==0 and y%100!=0)
def LastDay(m,y):
    if m==2:
        return 29 if Special(y) else 28
    return 31 if m in [1,3,5,7,8,10,12] else 30

d = int (input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

if d!= LastDay(m,y): print(d+1,m,y)
else :
    print((1,m+1,d) if m<12 else (1,1,y+1))
