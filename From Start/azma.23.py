#Kamel tarin
import random
import time
objects_lst=[]
lst=[]
id_list=[]
#Errors:
Error_001="{0} should be letter"
Error_002="{0} should be number and the lengh of {0} should be 10"
Error_003="This option does not supported"

def g(item):
    j=input(item).lower().strip().capitalize()
    return j
def ch_g():
    return input("Change= ").lower().strip().capitalize()
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
                        print(Error_003)
                        continue
                else:
                    print("Complete the operation")
                    continue
    def change(self,index):
        old_value=self.list[index]
        lst.remove(self.list)
        self.list[index]=ch_g()
        while True:
            print("Options: Accept | Back")
            chg_a=input("Option= ").lower().strip()
            if chg_a=="back":
                print(f"Don't Saved: {self.list[index]}")
                self.list[index]=old_value
                lst.append(self.list)
                break
            elif chg_a=="accept":
                print(f"Saved: {self.list[index]}")
                lst.append(self.list)
                break
            else:
                print(Error_003)
                continue
def main():
    while True:
        try:
            print("Options: Add | Show | Help | Info | Exit")
            s=input("Option= ").lower().strip()
            if s=="exit":
                print("Exiting...")
                return
            elif s=="help":
                print()
                continue
            elif s=="info":
                print()
                continue
            elif s=="add":
                obg=C()
                obg.add()
                objects_lst.append(obg)
                print()
            elif s=="show":
                while True:
                    print("Options: Student | Teacher | Back")
                    who=g("Which one are you? ")
                    if who=="Teacher":
                        print("Type password")
                        ps=g("Password =  ")
                        for _ in range(3):
                            if ps=="1234":
                                break
                            else:
                                print("Password is incorrect")
                                ps=g("Password =  ")
                        else:
                            #return
                            break
                        print("lists:")
                        print()
                        for i in lst:
                            print(i)
                            print()
                        while True:
                            print("Options: Change | Back")
                            print()
                            op_t=input("Option= ").lower().strip()
                            if op_t=="back":
                                break
                            elif op_t=="change":
                                attempt=0
                                while attempt<3:
                                    print("Type ID")
                                    try:
                                        g_id=int(g("ID =  "))
                                    except ValueError:
                                        print("ID should be Number")
                                        continue
                                    found=None
                                    for o in objects_lst:
                                        if o.ID==g_id:
                                            found=o
                                            break
                                    if found:
                                        break 
                                    else:
                                        attempt+=1
                                        print(f"Student with (ID: {g_id}) is NOT exist")
                                else:
                                    #return
                                    break
                                print()
                                while True:
                                    print("OPtion: First Name | Last Name | Phone Number | Code Melee | Back")
                                    wch=input("Option= ").lower().strip()
                                    if wch=="back":
                                        break
                                    elif wch=="first name":
                                        found.change(0)
                                        continue
                                    elif wch=="last name":
                                        found.change(1)
                                        continue
                                    elif wch=="phone number":
                                        found.change(2)
                                        continue
                                    elif wch=="code melee":
                                        found.change(3)
                                        continue
                                    else:
                                        print(Error_003)
                                        continue
                                continue
                            else:
                                print(Error_003)
                                continue
                        continue
                    elif who=="Student":
                        attempt=0
                        while attempt<3:
                            print("Type ID")
                            try:
                                g_id=int(g("ID =  "))
                            except ValueError:
                                print("ID should be Number")
                                continue
                            found=None
                            for o in objects_lst:
                                if o.ID==g_id:
                                    found=o
                                    break
                            if found:
                                break 
                            else:
                                attempt+=1
                                print(f"Student with (ID: {g_id}) is NOT exist")
                        else:
                            #return
                            break
                        
                        print(f"Your list:")
                        print()
                        print(found.list)
                        while True:
                            print("Options: Change | Back")
                            op_s=g("Option= ")
                            if op_s=="Back":
                                break
                            elif op_s=="Change":
                                while True:
                                    print("OPtion: First Name | Last Name | Phone Number | Code Melee | Back")
                                    wch=input("Option= ").lower().strip()
                                    if wch=="back":
                                        break
                                    elif wch=="first name":
                                        found.change(0)
                                        continue
                                    elif wch=="last name":
                                        found.change(1)
                                        continue
                                    elif wch=="phone number":
                                        found.change(2)
                                        continue
                                    elif wch=="code melee":
                                        found.change(3)
                                        continue
                                    else:
                                        print(Error_003)
                                        continue
                                continue
                            else:
                                print(Error_003)
                                continue

                        #if you want to go to main page [farsi(bejaye)] continue write break
                        continue
                    elif who=="Back":
                        break
                    else:
                        print(Error_003)
                        continue
                continue
            else:
                print(Error_003)
        except ValueError:
            print("Please type number (or) exit")
main()
