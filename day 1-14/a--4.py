while True:
    #Captal in first of string
    s=input("String=").lower().strip()
    #Way 1
    s=list(s)
    s[0]=s[0].upper()
    s="".join(s)
    print(s)
    #Way 2
    s=s[0].upper()+s[1:]
    print(s)
    #Way 3
    s=s.capitalize()
    print(s)
    