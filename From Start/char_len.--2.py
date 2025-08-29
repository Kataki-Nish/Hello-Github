#char_len.--2
while True:
    #string
    s=input("String=").lower()
    #number of a and e
    print("Number of (a)="+str(len([a for a in s if a=="a"])))
    print("Number of (e)="+str(len([e for e in s if e=="e"])))