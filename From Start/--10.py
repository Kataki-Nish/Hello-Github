while True:
    x=int(input("x="))
    t=1
    for i in range(x):
        i+=1
        t*=i
    print("x!="+str(t))
