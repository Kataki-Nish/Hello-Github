while True:
    mydict={"Errors":{1:"a",2:"b"},"Message":"Hi"}
    d=input("Input= ").lower().strip().capitalize()
    x=mydict.get(d,"NOT Exist")
    #print(x)
    #print(mydict)
    X=5.6
    del X
    if X.is_integer():
        print(10)
    else:
        print(f"Not {10}")
    if x.isdigit() or x.isalpha():
        print(20)
    elif isinstance(x,dict):
        print(30)
    del mydict["Errors"][1]
    print(mydict)
    print(f"not {10}")