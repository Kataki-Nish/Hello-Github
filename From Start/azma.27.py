#n=input("Name= ").lower().strip().capitalize()
student={"name":"Ali","age":20}
#student.update({"name":n})
#student.setdefault("CS",12)
#info={"City":"Tehran","Year":2025}
#student.update({"GPA":info})
#print(student)
#for k,v in student.items():
    #print(f"{f'{k.capitalize()}:': <5} {v}")
#print(f"{n: >5}")
del student["name"]
print(student)