s=input("Nhap S: ")
d=s.count("!")
if(d==0):
    s=s+"!!"
elif(d%2!=0):
    s=s+"!"
print("Chuoi S sau khi xu ly:",s)
