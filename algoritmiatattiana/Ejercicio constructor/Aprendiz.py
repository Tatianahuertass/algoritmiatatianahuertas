class Aprendiz:
    """"identificacion=''
    nombre=""
    edad=""
    email=""
    telefono="""""
#Mtetodo Constructor
def __init__(self,identificacion,nombre,edad,email,telefono):
            self.identificacion=identificacion
            self.nombre=nombre
            self.edad=edad
            self.email=email
            self.telefono=telefono
#Metodos
#def setidentificacion(self,identificacion):
    #self.identificacion=identificacion
def getidentificacion(self):
    return self.identificacion
#def setnombre(self,nombre):
    #self.nombre=nombre
def getnombre(self):
    return self.nombre
#def setedad(self,edad):
    #self.edad=edad
def getedad(self):
    return self.edad
#def setemail(self,email):
    #self.email=email
def getcorreo(self):
    return self.email
#def settelefono(self,telefono):
    #self.telefono=telefono
def gettelefono(self):
    return self.telefono

def calcularedad():
    if edad < 17:
        print(":::Es Menor De Edad:::")
    if edad > 18:
        print(":::Es Mayor De Edad:::")

i=1
identificacion=int(input("Ingrese Identificacion: "))
nombre=input("Ingrese Nombre:  ")
edad=int(input("Ingrese Edad:  "))
email=input("Ingrese Email:  ")
telefono=int(input("Ingrese Telefono:  "))

calcularedad()
aprendiz1=Aprendiz()

print("::: APRENDIZ 1:::")
print("Identificacion: ",identificacion)
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Email: ",email)
print("Telefono: ",telefono)

i=int(input('desea continua?1 para seguir 0 para salir'))

identificacion=int(input("Ingrese Identificacion: "))
nombre=input("Ingrese Nombre:  ")
edad=int(input("Ingrese Edad:  "))
email=input("Ingrese Email:  ")
telefono=int(input("Ingrese Telefono:  "))

calcularedad()
aprendiz2=Aprendiz()
print("::: APRENDIZ 2:::")
print("Identificacion: ",identificacion)
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Email: ",email)
print("Telefono: ",telefono)


