a=int(input("A = "))
b=int(input("B = "))
c=int(input("C = "))
if a < b < c:
    print("Xep tang dan: %d %d %d" % (a, b, c))
elif b <a < c:
    print("Xep tang dan: %d %d %d" % (b, a, c))
elif c<b < a:
    print("Xep tang dan: %d %d %d" % (c, b, a))
elif b <c <a:
    print("Xep tang dan: %d %d %d" % (b, c, a))
elif c <a <b:
    print("Xep tang dan: %d %d %d" % (c, a, b))
elif a<c < b:
    print("Xep tang dan: %d %d %d" % (a, c, b))
elif a==b<c:
    print("Xep tang dan: %d %d" %(b,c))
elif a==c<b:
    print("Xep tang dan: %d %d" %(c,b))
elif c==b<a:
    print("Xep tang dan: %d %d" %(b,a))
elif a<b==c:
    print(f"Xep tang dan: {a} {b}")
elif b<a==c:
    print(f"Xep tang dan: {b} {a}")
elif c<b==a:
    print(f"Xep tang dan: {c} {a}")
elif a==b==c:
    print(f"Xep tang dan: {c}")
    
    

