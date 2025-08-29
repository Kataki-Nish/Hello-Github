import math as m
while True:
    n=input("Number=")
    while n=="":
        print("Type number")
        n=input("Number=")
    n=int(n)
    while n<=1:
        print("Number should be more than 1")
        n=int(input("Number="))
    A=set()
    y=False
    for i in range(1,int(m.sqrt(n)+1)):
        if n%i==0:
            A.add(i)
            if i!=1:
                y=True
            if i!=n//i:
                A.add(n//i)
    if y:
        print("Number=Moracab")
    else:
        print("Number=Aval")
    print(sorted(A))