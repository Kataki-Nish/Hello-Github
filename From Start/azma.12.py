def if_s(a1):
    s=input(a1).lower().strip().capitalize()
    if s=="Exit":
        return "ext"
    elif s=="Help":
        return "hlp"
    return s
###Error unknown error
###Error this class isn't what I need
class sign:
    def __init__(self,item):
        self.item=item
        self.value=None
    def loop(self):
        while True:
            self.value=if_s(self.item)
            if self.value=="ext":
                break
            elif self.value=="hlp":
                print("Write Name (and) Age (and) City")
                continue
K=[sign("Name="),sign("Age="),sign("City=")]
print(f"Name={K[0]} Age={K[1]} City={K[2]}")          