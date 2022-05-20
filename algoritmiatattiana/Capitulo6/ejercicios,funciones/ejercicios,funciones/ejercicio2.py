#diseñe un algoritmio que defina una lista vacia
"""lista=[]
menor=[0]
#luego, agregue valores a la lista
n=int(input('Digite un numero entero: '))
for i in range(n):
    if [i]<menor:
        menor=n[i]
    lista.append(i)
    

print(lista)
print(len(menor))"""

#teniendo encuenta su longitud que debe ser menor a la digitada por el usuario

def fn(lst):
    lst = []
    mnro = [0]
    n=int(input('Digite un numero entero: '))
    for i in range(n):
        if [i] < mnro:
            mnro=n[i]
        lst.append(i)
    print(lst)
    print(len(mnro))

lst = []
mnro = [0]
fn(lst)


