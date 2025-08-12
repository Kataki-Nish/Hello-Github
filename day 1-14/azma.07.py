while True:
    try:
        print("Set (,) between number")
        n=input("[").strip().lower()
        print("]")
        if n=="":
            print("\u2205")
            continue
        if n=="help":
            print("PLease type number in list (or) exit")
            continue
        if n=="exit":
            break
        N1=["\u2205" if l=="" else float(l) for l in [t.strip() for t in n.split(",")]]
        #N2=["\u2205" if i==" " else ('Possetive' if i>0 else (0 if i==0 else 'Negetive')) for i in N1]
        #N2=['Possetive' if i>0 else (0 if i==0 else ('Negetive' if i<0 else i)) for i in N1]
        ###Error (only one space can get and if there are more than 1 space in {n} it send an Error)
        N2=[i if i=="\u2205" else('Possetive' if i>0 else (0 if i==0 else 'Negetive'))for i in N1]
        print(N2)
    except ValueError:
        print("Please type number in the list (or) exit")
