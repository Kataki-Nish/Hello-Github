###Error sum_args methood is not complete
class C:
    def __init__(self,*args,**kargs):
        self.args=args
        self.arg1=args[0]
        self.arg2=args[1]
        self.extrakey=kargs
    def sum_args(self,*numbers,**knumbers):
        if not knumbers:
            if not numbers:
                print(0)
            else:
                print((self.arg1+self.arg2)*sum(numbers))
        else:
            if not numbers:
                v=(self.arg1+self.arg2)
                for k in knumbers.keys():
                    if k!="t":
                        print(f"Error: This method does not support the keyword named {k}")
                        return
                    else:
                        g=v**knumbers[k]
                print(g)
            else:
                v=((self.arg1+self.arg2)*sum(numbers))
                for k in knumbers.keys():
                    if k!="t":
                        print(f"Error: This method does not support the keyword named {k}")
                        return
                    else:
                        g=v**knumbers[k]
                print(g)
p=C(3,2,l=4,s=5)
print(p.arg1)
print(p.extrakey)
print(p.extrakey["l"])
print(type(p.arg1))
print(type(p.args))
print(type(p.extrakey["l"]))
p.sum_args()
p.sum_args(4,3)
p.sum_args(t=2)
p.sum_args(4,3,t=2,t=3)
p.sum_args(c=3)