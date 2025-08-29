class chk:
    def __init__(self,prompt):
        self.prompt=prompt
        self.value=None
    def check(self):
        self.value=input(self.prompt).lower().strip().capitalize()
        if self.value=="Exit":
            return "ext"
        elif self.value=="Help":
            return "hlp"
        return self.value
###Error if Age==string program cant say the user age should be number
def main():
    K=[chk("Name="),chk("Age="),chk("City=")]
    while True:
        for item in K:
            result=item.check()
            if result=="ext":
                print("Exiting...")
                return
            elif result=="hlp":
                print("Write Name (and) Age (and) City")
                break
        else:
            print([f"{item.prompt.strip('=')}={item.value}" for item in K])
main()

