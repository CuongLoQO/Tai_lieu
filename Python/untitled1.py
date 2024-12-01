# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:48:31 2022

@author: Admin
"""
def S(a,b,c):
    if a<=0 or b<=0 or c<=0: return 0
    if a+b<=c or b+c<=a or c+a<=b: return 0
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
a=float(input("Do dai A = "))
b=float(input("Do dai B = "))
c=float(input("Do dai C = "))
d=float(input("Do dai D = "))
s=S(a,b,c) + S(a,b,d) + S(a,c,d) + S(b,c,d)
print("Ket qua =",-1 if s == 0 else '{:.5f}'.format(s))

2
