p=[("ali",20),("sara",22),("mohamad",19)]
result={n:{"Age":a,"Status":s} for n,a,s in ((n,a,"adult") if a>=20 else (n,a,"teen") for n,a in (i for i in p))}
print(result)