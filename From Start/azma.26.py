lst=[1,2,3,4,5,6]
squre_n={n:n**2 for n in lst}
print(squre_n)
cube_zoog={a:a**3 if a%2==0 else a for a in lst}
print(cube_zoog)
lst2=["apple","banana","kiwi"]
len_word={w:len(w) for w in lst2}
print(len_word)