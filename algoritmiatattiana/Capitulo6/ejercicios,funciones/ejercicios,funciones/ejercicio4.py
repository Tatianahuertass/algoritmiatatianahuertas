#Crear un diccionario de géneros literarios con el siguiente contenido:

#Narrativa:La Vorágine,Don Quijote de la mancha,Con la soga al cuello
#Dramatico:El hechizo del agua,Primero es ella,Hasta que salga el sol
#Lirico:Los Heraldos negros,Los versos del capitán,Cantar de Mio Cid

#Se debe mostrar la información organizada por categorías


def gne1():
    a=('Narrativa')
    print(a)
gne1()
def gnng():
    narrativo={1:'La Voragine',
                2:'Don Quijote de la mancha',
                3:'Con la soga al cuello'}
    for i,m in narrativo.items():
        print(i,m,end='\n')
    return i,m 
gnng()

def gne2():
    b=('Dramatico')
    print(b)
gne2()
def gnl():
    dramatico={1:'El hechizo del agua',
                2:'Primero es ella',
                3:'Hasta que salga el sol'}
    for t,s in dramatico.items():
        print(t,s,end='\n')
    return t,s
gnl()

def gn3():
    c=('Lirico')
    print(c)
gn3()
def gnnl():
    lirico={1:'Los Heraldos negros',
            2:'Los versos del capitan',
            3:'Cantar de Mio Cid'}
    for a,d in lirico.items():
        print(a,d,end='\n')
    return a,d
gnnl()




