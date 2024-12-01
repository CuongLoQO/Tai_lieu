s = input("Nhap chuoi: ")

if s[-3:] == '!!!':
    print("Chuoi sau khi bo sung dau cham than: '%s'" %s)
elif s[-2:] == '!!':
    print("Chuoi sau khi bo sung dau cham than: '%s!'" %s)
elif s[-1:] == '!':
    print("Chuoi sau khi bo sung dau cham than: '%s!!'" %s)
else:
    print("Chuoi sau khi bo sung dau cham than: '%s!!!'" %s)