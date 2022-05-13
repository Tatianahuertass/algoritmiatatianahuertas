def notas_estudiantes(n1,n2, n3):
    return print(dict(carmen=n1,carlos=n2, has=n3))

notas_estudiantes(4.0, 3.9, 5.0)

prom=notas_estudiantes/3
if (prom>=3):
    print('su promedio es: ',prom)
