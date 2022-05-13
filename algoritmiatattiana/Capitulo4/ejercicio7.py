tecla1=input('digite la primera tecla: ')
tecla2=input('digite la segunda tecla: ')
tecla3=input('digite la tercera tecla: ')
if tecla1=='ctrl' and tecla2=='alt' and tecla3=='del':
    print('cerrar sesion')
elif tecla1=='super':
    print('abre la busqueda de actividades')
elif tecla1=='ctrl' and tecla2=='alt' and tecla3=='t':
    print('atajo de terminal de ubuntu')
elif tecla1=='ctrl' and tecla2=='alt' and tecla3=='l' or tecla1=='super' and tecla2=='l':
    print('bloquea la pantalla')
elif tecla1=='ctrl' and tecla2=='alt' and tecla3=='d' or tecla1=='super' and tecla2=='d':
    print('mostrar escritorio')
elif tecla1=='super' and tecla2=='a':
    print('muestre el menu de la aplicacion')
elif tecla1=='super' and tecla2=='tab' or tecla1=='alt' and tecla2=='tab':
    print('cambiar entre aplicaciones en ejecucion')
elif tecla1=='super' and tecla2=='<' or tecla1=='super' and tecla2=='<':
    print('ajustar ventanas')
elif tecla1=='super' and tecla2=='m':
    print('alternar bandeja de notificaciones')
elif tecla1=='super' and tecla2=='space':
    print('cambiar teclado de entrada (para configuracion multilingue)')
elif tecla1=='ctrl' and tecla2=='q' or tecla1=='ctrl' and tecla2=='w' or tecla1=='alt' and tecla2=='f4':
    print('cerrar una ventana de aplicacion')
elif tecla1=='ctrl' and tecla2=='alt' and tecla3=='flecha':
    print('moverse en espacios de trabajo')
else:
    print('error')
    
    