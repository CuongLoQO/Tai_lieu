def sdx(n): 
    flag =0;
    if ( n[::-1] == n):
      flag = 1
    return flag
n = input("Nhap chuoi S: ")
check = sdx(n)
if check == 1:
    print(n,"co dang doi xung")
else:
    print(n,"khong co dang doi xung")
