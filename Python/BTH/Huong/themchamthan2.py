s = input("Nhap S: ")

if s[-3:] == '!!!':
    print("Chuoi S sau khi xu ly: %s" %s)
elif s[-2:] == '!!':
    print("Chuoi S sau khi xu ly: %s!" %s)
elif s[-1:] == '!':
    print("Chuoi S sau khi xu ly: %s!!" %s)
else:
    print("Chuoi S sau khi xu ly: %s!!!" %s)