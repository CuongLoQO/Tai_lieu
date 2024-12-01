A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if (A == B == C):
    print("Xep tang dan:",A)

if (A == B or A == C):
    if (A > B):
        A, B = B, A
        print("Xep tang dan:",A, B)
    elif (A < B):
        print("Xep tang dan:",A, B)
    elif (A > C):
        A, C = C, A
        print("Xep tang dan:",A, C)
    elif (A < C):
        print("Xep tang dan:",A, C)
   
elif (B == C):
    if (A > B):
        A, B = B, A
        print("Xep tang dan:",A, B)
    elif (A < B):
        print("Xep tang dan:",A, B)

elif (A != B and B != C and A != C):
        if (A > B):
            A, B = B, A
        if (A > C):
            A, C = C, A
        if (B > C):
            B, C = C, B
        print("Xep tang dan:",A, B, C)