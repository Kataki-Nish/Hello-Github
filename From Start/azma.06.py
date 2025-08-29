while True:
    try:
        n=input("Number=").lower().strip()
        while n=="":
            print("Type number")
            n=input("Number=").lower().strip()
        if n=="help":
            print("PLease type number (or) exit")
            continue
        if n=="exit":
            break
        n=float(n)
        print(f"Number {'should be between 1 and 0' if n>1 or n<0 else ('is in progress' if n<0.5 else f'is {n:.2%}')}")
    except ValueError:
        print("PLease type number (or) exit")