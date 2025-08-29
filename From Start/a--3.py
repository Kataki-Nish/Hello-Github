while True:
    s=input("String=").lower().strip()
    #Numer of char in string
    #Way 1
    A=len("".join(s.split()))
    print(A)
    #Way 2
    B=0
    for i in s:
        if i==" ":
            continue
        else:
            B+=1
    print(B)
    #way 3
    C=len("".join(["" if i==" " else i for i in s]))
    print(C)
    #Numer of word in string
    #Word 1
    D=len(s.split())
    print(D)