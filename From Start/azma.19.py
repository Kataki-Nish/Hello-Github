
import random
import time
objects_lst=[]
lst=[]
id_list=[]
def g(item):
    j=input(item).lower().strip().capitalize()
    return j
class C:
    def __init__(self):
        self.list=[]
        self.fname=None
        self.lname=None
        self.phone=None
        self.cdml=None
        self.accept=None
        self.ID=None
    def add(self):
        Error_001="{0} should be letter"
        Error_002="{0} should be number and the lengh of {0} should be 10"
        while True:
            while True:
                s1=g("First Name =  ")
                if s1:
                    if s1.isalpha():
                        self.fname=s1
                        self.list.append(self.fname)
                        break
                    else:
                        print(Error_001.format("First Name"))
                        continue
                else:
                    print("Write First Name")
                    continue
            while True:
                s2=g("Last Name =  ")
                if s2:
                    if s2.isalpha():
                        self.lname=s2
                        self.list.append(self.lname)
                        break
                    else:
                        print(Error_001.format("Last Name"))
                        continue
                else:
                    print("Write Last Name")
                    continue
            while True:
                s3=g("Phone Number =  +98 ")
                if s3:
                    if s3.isdigit() and len(s3)==10:
                        self.phone=s3
                        self.list.append(f"0{self.phone}")
                        break
                    else:
                        print(Error_002.format("Phone Number"))
                        continue
                else:
                    print("Write Phone Number")
                    continue

            while True:
                s4=g("Code Melee =  ")
                if s4:
                    if len(s4)==10 and s4.isdigit():
                        self.cdml=s4
                        self.list.append(self.cdml)
                        break
                    else:
                        print(Error_002.format("Code Melee"))
                        continue
                else:
                    print("Write Code Melee")
            while True:
                a=self.accept
                print("Options: Accept | Back")
                a=g("Option =  ")
                if a:
                    if a=="Back":
                        self.list=[]
                        print("The operation does not registered")
                        return
                    elif a=="Accept":
                        id=random.randint(1000,9999)
                        while id in id_list:
                            id=random.randint(1000,9999)
                        self.ID=id
                        id_list.append(self.ID)
                        self.list.append(self.ID)
                        lst.append(self.list)
                        print(f"Saved: {self.list}")
                        print(f"Your ID is :  {self.ID}")
                        time.sleep(5)
                        return
                    else:
                        print("This option does not supported")
                        continue
                else:
                    print("Complete the operation")
                    continue
def main():
    while True:
        try:
            print("Options: Add | Show | Exit")
            s=input("Option=").lower().strip()
            if s=="exit":
                print("Exiting...")
                return
            elif s=="help":
                print()
                continue
            elif s=="add":
                obg=C()
                obg.add()
                objects_lst.append(obg)
                print()
            elif s=="show":
                while True:
                    print("opetions: Student | Teacher")
                    who=g("Which one are you? ")
                    if who=="Teacher":
                        print("Type password")
                        ps=g("Password =  ")
                        for _ in range(3):
                            if ps=="1234":
                                break
                            else:
                                print("Password is incorrect")
                        else:
                            return
                        print("list:")
                        print()
                        for i in lst:
                            print(i)
                            print()
                        input("For back press Enter")
                        break
                    elif who=="Student":
                        print("Type ID")
                        g_id=g("ID =  ")
                        
                        print()
                    else:
                        print("This option does not supported")
                        continue
                continue
            elif s=="change":
                print()
            else:
                print("This option does not supported")
        except ValueError:
            print("Please type number (or) exit")
main()
