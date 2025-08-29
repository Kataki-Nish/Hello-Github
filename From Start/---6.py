#ماشین حساب ساده V.002
# + - * / ^ = > <
inp=input()
if "+" in inp:
    part=inp.split("+")
    n1=float(part[0])
    n2=float(part[1])
    print(n1+n2)
elif "-" in inp:
    part=inp.split("-")
    n1=float(part[0])
    n2=float(part[1])
    print(n1-n2)
elif "*" in inp:
    part=inp.split("*")
    n1=float(part[0])
    n2=float(part[1])
    print(n1*n2)
elif "/" in inp:
    part=inp.split("/")
    n1=float(part[0])
    n2=float(part[1])
    if n2==0:
        print("Error:Division by zero is not allowed")
    else:
        print(n1/n2)
elif "^" in inp:
    part=inp.split("^")
    n1=float(part[0])
    n2=float(part[1])
    print(n1**n2)
elif "=" in inp:
    part=inp.split("=")
    n1=float(part[0])
    n2=float(part[1])
    print(n1==n2)
elif ">" in inp:
    part=inp.split(">")
    n1=float(part[0])
    n2=float(part[1])
    print(n1>n2)
elif "<" in inp:
    part=inp.split("<")
    n1=float(part[0])
    n2=float(part[1])
    print(n1<n2)

input()