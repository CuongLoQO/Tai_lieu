n = int(input("N = "))
j=0
k=0
list=[1]
for i in range(n-1):
    a = 2*list[j]+1
    b = 3*list[k]+1
    if a<b:
        j+=1
        list.append(a)
    elif b<a:
        k+=1
        list.append(b)
    else:
        k+=1
        j+=1
        list.append(a)
print(n,"so dau tien cua N23: ",end='')
for i in range(n):
   print(list[i], end=' ' if i < n-1 else '\n')
    
