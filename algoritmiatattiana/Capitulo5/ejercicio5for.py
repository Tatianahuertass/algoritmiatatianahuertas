a=[1, 20]
print(a)
for i in a:
    n=int(input('digite un numero entero: '))
    if n>0:
        print(a[n])
    elif n<0:
        print('\nDigite un numero positivo')
