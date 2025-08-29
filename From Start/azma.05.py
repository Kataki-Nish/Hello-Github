while True:
    try:
        pas=input("Type password ").lower().strip()
        for i in range(2):
            if i==1:
                if pas!="password":
                    print("password is incorrect")
                    pas=input("Type password ").lower().strip()
            elif 1<i<3:
                if pas!="incorrect":
                    print("try again")
                    pas=input("Type password ").lower().strip()
                
                

    except ValueError:
        print(12)