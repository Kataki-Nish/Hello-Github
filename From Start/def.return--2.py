def maxim(n1,n2,n3):
    return sorted({n1,n2,n3})[-1]
while True:
    a1=float(input("Number="))
    a2=float(input("Number="))
    a3=float(input("Number="))
    print("Max=",maxim(a1,a2,a3))