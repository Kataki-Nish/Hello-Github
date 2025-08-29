import math as m
def zoog(n1,n2):
    if n1>n2:
        n1,n2=n2,n1
    n1=m.ceil(n1)
    n2=int(n2)
    if n1%2==0:
        n1=n1
    else:
        n1=n1+1
    if n2%2==0:
        n2=n2
    else:
        n2=n2-1
    A=[i for i in range(n1,n2+1,2)]
    return A
while True:
    a1=float(input("Number(1)="))
    a2=float(input("Number(2)="))
    print(zoog(a1,a2))