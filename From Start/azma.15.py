class chk:
    def __init__(self,prompt):
        self.prompt=prompt
        self.value=None
    def check(self):
        self.value=input(self.prompt).lower().strip().capitalize()
        return self.value
def main():
    K=[chk("Name="),chk("Age="),chk("City=")]
    while True:
        try:
            for item in K:
                result=item.check()
                if result=="Exit":
                    print("Exiting...")
                    return
                elif result=="Help":
                    print("Write Name (and) Age (and) City")
                    break
                elif item==K[1]:
                    item.value=int(item.value)
            else:
                print([f"{item.prompt.strip('=')}={item.value}" for item in K])
        except ValueError:
            print("Error: Age should be integer")
main()