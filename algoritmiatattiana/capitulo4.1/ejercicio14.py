pro_h=0
pro_m=0
ch=0
cm=0
acu_h=0
acu_m=0
e_min=999
ingreso=str(input('desea ingresar?:'))

if ingreso=='si' or ingreso=='si' or ingreso=='si':
    
    
    while ingreso=='si' or ingreso=='si' or ingreso=='si':
        print('\nnuevo usuario')
        edad=int (input('que edad tiene: '))
        t_h_m=ch+cm
        
        if edad>=18:
            nombre=str(input('nombre completo: '))
            genero=str(input('genero: '))
            
            if edad<e_min and edad!=0:
                e_min=edad
                
            if  genero=='hombre':
                ch +=1
                acu_h=acu_h+edad
                pro_h=int(acu_h/ch)
            elif genero=='mujer':
                cm+=1
                acu_m=acu_m+edad
                pro_m=int(acu_m/cm)
                
        elif edad>0 and edad<18:
            print('no puedes ingresar, no tiene la edad requerida para el ingreso')
        else:
            break
    print(f'''\ntotal asistencias en la fiesta: {t_h_m}\ntotal asistencia de hombres: {ch}.\ntotal mujeres: {cm}
        \npromedio edad hombre: {pro_h} \npromedio edad mujeres: {pro_m}
        \nedad minima de personas que asistieron: {e_min}''')
else:
    print('salir de pagina')