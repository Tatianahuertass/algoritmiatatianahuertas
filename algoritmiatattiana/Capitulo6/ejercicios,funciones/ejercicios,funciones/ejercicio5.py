#Realizar un algoritmo que permita registrar y mostrar la información de 5 estudiantes de un
#colegio 

#Además de contar con un menú con las siguientes opciones: 
#ingresar estudiantes
#listar estudiantes
#modificar notas de un estudiante por codigo
#consultar la nota definitiva de un estudiante
#salir
print('\n')
print('1. ingresar estudiantes')
print('2. listar estudiantes')
print('3. modificar notas de un estudiantes por codigo')
print('4. consultar la nota definitiva de un estudiante')
print('5. salir')
#el registro estudiante está definido por:
#codigo de estudiante
cod=int(input('digite el codigo: '))
#nombre
nom=input('Digite su nombre: ')
#nota1 nota2
n1=float(input('Digite la nota1: '))
n2=float(input('Digite la nota2: '))
notas=(n1,n2)
#la definitiva de las notas es el promedio de las 2
#la nota oscilacion debe ser de 0.0 y 5.0

