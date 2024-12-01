import os


os.system("cls")

# print(sorted(input().split()))
# b1
#print([int(x) for x in input().split(",")])
# b2
#print([i for i in range(1, int(input())) if sum(x for x in range(1, i) if i % x == 0) <= i])
# b3
# print(tuple(i for i in range(2, 100) if len([j for j in range(2, int(i ** .5) + 1) if i % j == 0]) == 0))
# b4
(lambda s: print("Email ko dung dinh dang " if (s.count("@") != 1 != s.count(".") or s.index(".") - s.index("@") <= 1 or s.index("@") == 0 or s.index(".") == len(s) - 1) else "Email dung dinh dang"))(input())
# b6
# (lambda x: print([int((((((1 + 5 * .5) / 2) * i)) - ((((1 - 5 * .5) / 2) * i))) / (5 ** .5)) for i in range(x)]))(int(input()))
# b7
