from Aprendiz import aprendiz
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
aprendiz1=aprendiz()

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
aprendiz2=aprendiz()

print("::: APRENDIZ 2:::")
print("Identificacion: ",identificacion)
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Email: ",email)
print("Telefono: ",telefono)