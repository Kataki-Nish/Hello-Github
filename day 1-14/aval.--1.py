while True:
    n=int(input("Number="))
    for i in range(2,n):
        if n%i==0:
            print("Number=moracab")
            print("i="+str(i))
            break
    else:
        print("Number=aval")