
try:
    a=int(input("A = "))
    b=int(input("B = "))
    print(f'a/b = {a/b}')
except ValueError:
    print("Vui lòng nhập số nguyên")
except ZeroDivisionError:
    print("Vui lòng nhập b khác 0")
