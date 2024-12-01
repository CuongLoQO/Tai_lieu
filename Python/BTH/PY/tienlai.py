import math
tien = 1e7
print("Số tiền ban đầu là: ",tien)
lai=5.1/100
for i in range(0,10):
    x = tien*lai
    tien = tien + x
print("Số tiền sau 10 năm là: ",math.ceil(tien))
dem = 0
tien = 1e7
while(tien<5e7):
    x = tien*lai
    tien = tien + x
    dem=dem+1
print("Sau ",math.ceil(dem)," năm bạn sẽ có ít nhất 50 triệu")
