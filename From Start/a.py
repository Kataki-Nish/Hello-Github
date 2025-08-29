while True:
    s=input("String=").lower().strip()
    A=[i for i in s if i=='a']
    B=["" if i=="a" else i for i in s]
    print(B)
    C="".join(B)
    print(C)
    #delete space in string
    #Way 1
    D=s.split()
    E="".join(D)
    print("E=",E)
    #Way 2
    G="".join(s.split())
    print("G=",G)
    #Way 3
    F="".join(["" if i==" " else i for i in s])
    print("F=",F)
