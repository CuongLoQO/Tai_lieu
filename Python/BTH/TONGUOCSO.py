n = int(input("N = "))
sum = 0
for i in range (1, int((n**0.5)+1)):
    if n%i == 0:
        j=int(n/i)
        if i==j:
            sum=sum+i
        else:
            sum=sum+i+j
print("Tong cac uoc so cua", n,"la", sum)
