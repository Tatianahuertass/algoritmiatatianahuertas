f=input('Digite su fecha de nacimiento: ')
dia=int(input('Digite su dia: '))
mes=int(input('Digite su mes: '))
anio=int(input('Digite su anio: '))

sum=0
m3=dia+mes+anio   
print(f'la suma de su fecha de nacimiento de {f} es: ',m3)

sumdigito=0
extnum=0
n=int(input('Entonces ingrese los digitos de la suma: '))

while n!=0:
    extnum=n%10
    n=n//10
    sumdigito=sumdigito+extnum
print('su numero de suerte, segun su fecha de cumpleaños es: ',sumdigito)
    
