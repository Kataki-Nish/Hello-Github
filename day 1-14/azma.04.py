while True:
    try:
        pas=input("Type password ").lower().strip()
        while pas!="password":
            if pas=="incorrect":
                break
            else:
                print("password is incorrect")
                pas=input("Type password ").lower().strip()
        print("Welcome ^_^")
    except ValueError:
        print(12)