import math as m
while True:
    try:
        n=input("Number=").lower().strip()
        while n=="":
            print("Type number")
            n=input("Number=").lower().strip()
        if n=="help":
            print("PLease type integer number")
            continue
        if n=="exit":
            break
        n=float(n)
        while not n.is_integer():
            print("Number should be integer")
            n=float(input("Number=").lower().strip())
        n=int(n)
        print(f"Number is {'+' if  n>0 else '-' if n<0 else 0}")
    except ValueError:
        print("PLease type number (or) exit")