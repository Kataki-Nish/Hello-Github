#ماشین حساب ساده V.001
n1=float(input())
op=input()
n2=float(input())
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    if n2==0:
        print("Error:Division by zero is not allowed")
    else:
        print(n1/n2)
elif op=="^":
    print(n1**n2)

input("For exit press enter")