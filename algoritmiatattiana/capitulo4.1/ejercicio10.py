
from cgitb import text
from cgitb import texto

alfabetico=('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgjklmnopqrstuvwxyz')
texto=str(input(' digite la palabra: '))
contar=0

for i in texto:
    if texto in alfabetico:
        contar+=1
    else:
        print('se ha encontrado caracteres no alfabeticos')
        break
if contar==len(texto):
    print('todos los caracteres son alfabeticos')
    