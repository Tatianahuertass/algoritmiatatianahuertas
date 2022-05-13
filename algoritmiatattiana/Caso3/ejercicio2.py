fecha=input('Digite su fecha de nacimiento: ')
dia=int(input('Digite su dia: '))
mes=int(input('Digite su mes: '))
anio=int(input('Digite su anio: '))

sum=0
f=dia+mes+anio

while f >= 10:
    suma=0
        
    while f >0:
        r=f%10
        f=f//10
        suma=suma+r
    
    f=suma
        
print(f'El numero de la suerte, segun mi fecha de cumpleaños {fecha} es: ',f )