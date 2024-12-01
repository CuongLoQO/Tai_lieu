def lockitu(s):
    chuoikitu=""
    for i in s:
        if i not in chuoikitu:
            chuoikitu+=i
    return chuoikitu
def dem(s):
    for i in lockitu(s):
        dem=s.count(i)
        print("'{}' xuất hiện {} lần\n".format(i,dem),end='')
s=input("Nhap chuỗi: ")
dem(s)
