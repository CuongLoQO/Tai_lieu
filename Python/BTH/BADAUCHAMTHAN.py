s=input("Nhap chuoi: ")
print("Chuoi sau khi bo sung dau cham than:",end=' ')
if s.endswith('!!!'):
    print("\'"+s+"\'")
else:
    s = s+'!' if s.endswith('!!') else s+'!!' if s.endswith('!') else s+'!!!'
    print("\'"+s+"\'")


    
s=input("Nhap chuoi: ")
def themdau(s):
    s+='!'*(3-s[-3:].count('!'))
    return "\'"+s+"\'"
print('Chuoi sau khi bo sung dau cham than:',end=' ')
if s[-3:].count('!')>2:
    print("\'"+s+"\'")
else:
    print(themdau(s))
