p=[("ali",20),("sara",22),("mohamad",19)]
result={n.capitalize():{"Age":a,"Status":"adult" if a>=20 else "teen"} for n,a in p}
print(result)