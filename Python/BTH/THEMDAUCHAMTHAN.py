s = input("Nhap S: ")
while (s.endswith('!!!')==False):
    s = s + '!'
    if(s.endswith('!!!')==True):
        break
print("Chuoi S sau khi xu ly: ",s,sep=(""))
