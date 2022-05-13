n=int(input('digite un numero: '))
sumatoria=0
lista=[]

for i in range(1, n):
    if n%i==0:
        sumatoria=sumatoria+i
        lista.append(i)
if sumatoria==n:
    print(n, 'es un numero perfecto y sus divisiones propios son los siguientes numeros: ',lista)
else:
    print('no es perfecto y sus divsores son los siguientes numeros', lista)
