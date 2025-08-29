###Error: Cant use __new__ methood yet
class gint(int,object):
    def __new__(cls,*value):
        obg=super().__new__(cls,value)
        obg=obg.__int__()
        return obg
    def __init__(self,*value):
        self.value=value
a=gint(12.3)
print(isinstance(a,object))