#n=integer
import math as m
def aval(n):
    for i in range(1,int(m.sqrt(n)+1)):
        if i!=1:
            if n%i==0:
                print("Number=Not Prime")
                break
    else:
        print("Number=Prime")
while True:
    try:
        a=input("Number=")
        while a=="":
            print("Type number")
            a=input("Number=")
        a=a.lower()
        if a=="exit":
            break
        if a=="help":
            print("Please type number (or) exit")
            continue
        a=float(a)
        while a-float(int(a))>0:
            print("Number should be integer")
            a=float(input("Number="))
        a=int(a)
        while a<=1:
            print("Number should be more than 1")
            a=int(float(input("Number=")))
        aval(a)
    except ValueError:
        print("Please type number (or) exit")

    