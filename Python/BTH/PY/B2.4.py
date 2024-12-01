def total(n):
    return n%10 + total(n//10) if n > 9 else n

n=int(input("N = "))
s=2**n
print("Tong = "+str(total(s)))

