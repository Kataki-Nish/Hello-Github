#char_len.--1
while True:
    #string
    s=input('string=').lower()
    N_a=0
    N_e=0
    #char of string
    for char in s:
        #exist of a
        if char=="a":
            N_a+=1 
        #exist of e
        elif char=="e":
            N_e+=1
        else:
            continue
    #number of a and e
    print("Number of (a)="+str(N_a))
    print("Number of (e)="+str(N_e))

