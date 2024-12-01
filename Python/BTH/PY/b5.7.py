n=int(input("N = "))
list = [0]*1000000
a=[]
for i in range(3,n+1,2):
    if list[i] ==0:
        a.append(i)
        list[i]=1
        for k in range(i*i,n+1,i):
            list[k]=1
a=tuple(a)
print(a)
