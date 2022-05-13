print('este juego es piedra papel y tijera: ')
jugador1=input('jugador 1 elija su opcion: ')
jugador2=input('jugador 2 elija su opcion: ')
if (jugador1=='piedra') and (jugador2=='piedra'):
    print('han empatado porque han elegido la misma opcion')
elif (jugador1=='piedra') and (jugador2=='papel'):
    print('gana el jugador 2 porque el papel envuelve la piedra')
elif (jugador1=='papel') and (jugador2=='tijera'):
    print('gana el jugador 1 porque la piedra daña a la tijera')
elif (jugador1=='papel') and (jugador2=='piedra'):
    print('ha ganado el jugador 1 porque el papel envuelve la piedra')
elif (jugador1=='papel') and (jugador2=='papel'):
    print('han empatado porque han elegido la misma opcion')
elif (jugador1=='papel') and (jugador2=='tijera'):
    print('gana el jugador 2 porque el papel daña a la tijera')
elif (jugador1=='tijera') and (jugador2=='piedra'):
    print('ha ganado jugador 2 porque la tijera se daña con el papel')
elif (jugador1=='tijera') and (jugador2=='papel'):
    print('ha ganado jugador 1 porque la tijera corta papel')
elif (jugador1=='tijera') and (jugador2=='tijera'):
    print('han empatado porque han elijido la misma opcion')
