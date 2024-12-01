x = int(input("Nhap N duong: "))
a = 1
sum = 0
for i in range(1,x+1):
        a=a*i
        sum=sum+a
print("F(" + str(x) +")" + " = " + str(sum))
