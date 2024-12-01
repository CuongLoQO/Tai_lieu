def  F(n):
   if(n==0 || n==1) return 1;
    else return F(n-2) +F(n-1);

def CHECKFIBO(m):
    kt=0;      
    for(int i=0;i<=m;i++)
        if(F(i)==m) 
            kt=1
     return "True" if kt==1 else "Fales"

n = int(input("Nhập n: "))
CHECKFIBO(n)
