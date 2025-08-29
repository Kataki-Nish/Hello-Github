mesg={"op":{"flerror":"{0} should be float","inerror":"Age should be integer","fbetween":"{0} should be between 0 and 20","ibetween":"{0} should be between 6 and 18"},
    "name":{"letter":"Name should be letter","error2":"{0} already exist in students' list","1word":"Name should be 1 word"},
    "none":"Write {0}"}
L=["Age","Math","English"]
def gt(item):
    while True:
        x=input(f"{item}= ").lower().strip()
        if not x:
            print(mesg["none"].format(item))
            continue
        if item=="Age":
            try:
                x=int(x)
                if 6<x<=18:
                    return x
                else:
                    print(mesg["op"]["ibetween"].format(item))
                    continue
            except ValueError:
                print(mesg["op"]["inerror"])
                continue
        else:
            try:
                x=float(x)
                if 0<=x<=20:
                    return x
                else:
                    print(mesg["op"]["fbetween"].format(item))
                    continue
            except ValueError:
                print(mesg["op"]["flerror"].format(item))
                continue
student={}
while True:
    name=input("Name= ").lower().strip().capitalize()
    if not name:
        print(mesg["none"].format("Name"))
        continue
    elif len(list(name.split()))>1:
        print(mesg["name"]["1word"])
        continue
    elif not name.isalpha():
        print(mesg["name"]["letter"])
        continue
    #use generater expression in dict comprehension
    name_info={k:v if k=="Age" else v+2 for k,v in ((i,gt(i)) for i in L)}
    student.update({name:name_info})
    print(student)