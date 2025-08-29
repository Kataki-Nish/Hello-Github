lst=["ali","mohamad","sara"]
dict1={k:len(k) for k in lst}
print(dict1)
x="".join(input(" =  ").lower().strip().split())
y=sorted(set(x))
result={i:x.count(i) for i in y}
print(result)
number={n:n**2 if n%2==0 else n**3 for n in range(1,11)}
print(number)


