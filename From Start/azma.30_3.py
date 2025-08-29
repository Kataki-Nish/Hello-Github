#creat list
p=[("ali",20),("sara",22),("mohamad",19)]
#creat dict comprehension
result={n.capitalize():{k:(a if k=="Age" else ("adult" if a>=20 else "teen")) for k in ("Age","Status")} for n,a in p}
#creat generator expression
gen=((n.capitalize(),dict((k,(a if k=="Age" else ("adult" if a>=20 else "teen"))) for k in ("Age","Status"))) for n,a in p)
#print dict comprehension
print(result)
#print location of generator expression
print(gen)
#use generator expression
for i in gen:
    print(i)
#be cause we use gen then it is finished and now gen=None
result2=dict(gen)
print(result2)