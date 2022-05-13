#diseñe un algoritmo que capture la produccion de cafe del año 2021 y calcule:
#mes con mayor produccion y su valor
#menor produccion
#promedio
#meses estuvieron por encima del promedio
#meses por debajo del promedio

Meses=["Enero: ","Febrero: ","Marzo: ","Abril: ","Mayo: ","Junio: ","Julio: ","Agosto: ","Septiembre: ","Octubre: ","Noviembre: ","Diciembre: "]
v_i=[]

for i in Meses:
    Valores=int(str(input("Ingrese los valores de la produccion de cafe de {} ".format(i))))
    v_i.append(Valores)

promedio=sum(v_i)/len(Meses)
mayor=max(v_i)
minimo=min(v_i)

index_max=max(range(len(v_i)), key=v_i.__getitem__)
print("el valor mayor es {}, corresponde al mes de {}".format(mayor,Meses[index_max]))

index_min=min(range(len(v_i)), key=v_i.__getitem__)
print("el valor menor es {}, corresponde al mes de {}".format(minimo,Meses[index_min]))

print("el promedio de los valores es {} ".format(promedio))

print("valores mayores al promedio")
for i in range(len(v_i)):
    if v_i[i]> promedio:
        print(" {}, corresponde al mes de {}".format(v_i[i], Meses[i]))

print("valores mayores al promedio")
for i in range(len(v_i)):
    if v_i[i]> promedio:
        print(" {}, corresponde al mes de {}".format(v_i[i], Meses[i]))