while True:
    s=input("Strinng=").lower()
    print(s.strip('b'))
    print("Lengh(a)="+str(s.count("a")))
    s=s.replace("a","A")
    print(s)
