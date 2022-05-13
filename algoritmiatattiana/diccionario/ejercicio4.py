palabra='boom'
dict={}

for c in palabra:
    dict[c]=dict.get(c, 0)+1

print(dict)