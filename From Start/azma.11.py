def if_s(a1):
    s=input(a1).lower().strip().capitalize()
    if s=="Exit":
        return "ext"
    elif s=="Help":
        return "hlp"
    return s
###Error class should be not in loop 
###Error break should be not in class
###Error self in class cant be changed
while True:
    class check:
        def __init__(self,item):
            self.item=item
        def chk(self):
            self=if_s(self.item)
            if self=="ext":
                break
            elif self=="hlp":
                print("Write Name (and) Age (and) City")
                continue
    K=[check("Name="),check("Age="),check("City=")]
    print(f"Name={K[0]} Age={K[1]} City={K[2]}")