def Cap(t):
    #t=t.split()
    #for i  in t:
        #   i=i[0].upper()+i[1:]
    #t=" ".join(t)
    return " ".join([i[0].upper()+i[1:] for i in (t.split())])
while True:
    try:
        s=input().lower().strip()
        #s=s.split()
        #s=" ".join([i.capitalize() for i in s])
        s=Cap(s)
        print(s)
        n=s.count("a")+s.count("A")
        print(n)
        print(s.replace("a","@").replace("A","@"))
    except ValueError:
        print()