#dada una lista 10 elementos
#recorrer la lista y mostrar el contenido de la lista
def elemento():
    list=[1,2,3,4,5,6,7,8,9,10]
    print(list)
    return lista
#hacer una funcion que recorra la lista y devuelva una cadena con los valores de la lista
def devolver(lista):
    print(','.join(map(str,lista)))
        
def listaordenada(lista):
    print(sorted(lista))
#ordenar de mayor a menor
def mayor_a_menor(lista):
    lista.sort(reverse=True)
    print(lista)

#buscar un elemento que el usuario pida por teclado
#mostar su tamaño o longitud
def elemmento(lista):
    if  n in lista:
        lista.index(n)
        print(f'la longitud de la lista es: ',len(lista))
        
#programa principal
lista=[1,2,3,4,5,6,7,8,9,10]
elemento()
devolver(lista)
listaordenada(lista)
mayor_a_menor(lista)
n=int(input('digite el elemento que desea buscar: '))
print(lista.index(n))
elemmento(lista)


