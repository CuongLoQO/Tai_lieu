list = [5000, 2000, 1000, 500, 200]
def back(n, m, i=0, soto=0, sotien=0):
    ii=0
    if (i>4): return 0
    if i==4:
        if (n-sotien)%list[4]==0 and (n-sotien)//list[4]+soto<=m: return 1
        else: return 0
    else:
        for j in range(max(0, ((n-sotien)-(m-soto)*list[i+1])//list[i]), m-soto+1):
            tmp=sotien+j*list[i]
            if tmp==n: ii+=1
            elif tmp<n:
                ii+=back(n, m, i+1, soto+j, tmp)
            else: return ii
        return ii
n=int(input("N = "))
m = int(input("M = "))
print(f"Co {back(n, m)} phuong an doi tien")
