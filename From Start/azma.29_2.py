mesg={"op":{"flerror":"{0} should be float","inerror":"Age should be integer","none":"Write {0}"},"name":{"error1":"Name should be letter","error2":"{0} already exist in students' list"}}
K=["Age","Math","English"]
def gt(item):
    while True:
        x=input(f"{item}= ").lower().strip()
        if not x:
            print(mesg["op"]["none"].format(item))
            continue
        if item=="Age":
            try:
                x=int(x)
                return x
            except ValueError:
                print(mesg["op"]["inerror"])
                continue
        else:
            try:
                x=float(x)
                return x
            except ValueError:
                print(mesg["op"]["flerror"].format(item))
                continue
student={}
while True:
    name=input("Name= ").lower().strip().capitalize()
    if not name.isalpha():
        print(mesg["name"]["error1"])
        continue
    name_info={o:gt(o) if o=="Age" else gt(o)+2 for o in K}
    student.update({name:name_info})
    print(student)