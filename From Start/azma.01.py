while True:
    s=input("String=").lower().strip()
    #sliceing
    A=s[1:-1]
    B=s[-2:0:-1]
    C=s[-2:]
    D=s[0].upper()+s[1:-1]+s[-1].upper()
    print(A)
    print(B)
    print(C)
    print(D)