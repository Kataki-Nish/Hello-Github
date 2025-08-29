#Begginer Way
def main():
    lst=[]
    while True:
        try:
            print("Options: Add | Show | Exit")
            s1=input("Option=").lower().strip()
            if s1=="exit":
                print("Exiting...")
                return
            elif s1=="help":
                print("Chose one of options\n if you chose add the number you give will add to list \n if you chose show the sum of numbers in the list will appear \n if you chose the exit program will close")
                print()
                continue
            elif s1=="add":
                while True:
                    try:
                        s2=input("Number=").lower().strip()
                        while s2=="":
                            print("Type number")
                            s2=input("Number=").lower().strip()
                        if s2=="back":
                            break
                        elif s2=="help":
                            print("Type integer number (or) back")
                            continue
                        s2=float(s2)
                        while not s2.is_integer():
                            print("Number should be integer")
                            s2=float(input("Number=").lower().strip())
                        s2=int(s2)
                        lst.append(s2)
                        print(f"{s2} added to the list")
                        break
                    except ValueError:
                        print("Please type integer number (or) back")
            elif s1=="show":
                t=0
                for i in lst:
                    t+=i
                print(f"Sum of numbers =  {t}")
                continue
            else:
                print("This option does not supported")
        except ValueError:
            print("Please type number (or) exit")
main()