n=int(input("N = "))
sum=0
for i in range(1,n+1,2):
    sum+=i*i
print(f'F{n} = {sum}')
