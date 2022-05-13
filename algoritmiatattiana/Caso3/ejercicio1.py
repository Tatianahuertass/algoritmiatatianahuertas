#Elabore un algoritmia que simule el seguiente juego:
#-se debe asignar a cada persona su numero de suerte , este numero se obtiene con la siguiente formula:

#Se pide al usuario la fecha de nacimiento
#Se suman los digitos de la fecha de nacimiento 
#Se suma nuevamente los digitos del resultado hasta obtener un solo digito

fecha=input('Digite su fecha de nacimiento: ')

i=1
suma=0
#while f >= 10:
    #suma=0
        
while i!=0:
    dia=int(input('Digite su dia: '))
    mes=int(input('Digite su mes: '))
    anio=int(input('Digite su anio: '))
    f=dia+mes+anio
    r=f%10
    f=f//10
    suma=suma+r
    
    i=suma
        
    print(f'El numero de la suerte, segun mi fecha de cumpleaños {fecha} es: ',f )

    i=int(input('desea continua?1 para seguir 0 para salir'))



