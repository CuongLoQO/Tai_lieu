x = int(input("X = "))
dem = 0
while (x>0):
    dem=dem+1
    y=x
    x=int(x/10)
print("X có ", dem," chữ số")
print("Chữ số đầu tiên trong X là: ",y)
