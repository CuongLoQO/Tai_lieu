n=int(input("N = "))
m=int(input("M = "))
s=0
for i in range(0,m+1):
    x=n-i*5000
    if(x<0):
        break
    for j in range(0,m+1):
        y=x-j*2000
        if(y<0):
            break
        for k in range(0,m+1):
            z=y-k*1000
            if(z<0):
                break
            for h in range(0,m+1):
                t=z-h*500
                if(t<0):
                    break
                for l in range(0,m+1):
                    u=t-l*200
                    if(u==0) and (i+j+k+h+l) <=m :
                        s=s+1
print("Co {0} phuong an doi tien".format(s))
