def contabilizandofocosEDCHP():
    focosverdes = 0
    focosblancos = 0
    focosrojos = 0
    S = int (input ('Ingrese el valor de S: '))
    for i in range (1, S + 1):
        print ("PROCESO ",  (i))
        print ("Seleccione el valor de color.")
        print ("1.- verde")
        print ("2.- blanco")
        print ("3.- rojo")
        color = 0
        while color<1 or color>3:
            color = int (input (': '))
        if color==1:
            focosverdes=focosverdes+1
        if color==2:
            focosblancos=focosblancos+1
        if color==3:
            focosrojos=focosrojos+1
        print ()
    print (F"Valor de focos verdes:{focosverdes} " )
    print (F"Valor de focos blancos:{focosblancos} ")
    print (F"Valor de focos rojos:{focosrojos} " )
contabilizandofocosEDCHP()