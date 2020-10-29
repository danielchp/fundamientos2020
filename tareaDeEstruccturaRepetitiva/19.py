def impuestoautomovilesEDCHP():
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    impuestoapagar = 0
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        clave = float (input ('Ingrese el valor de clave: '))
        costo = float (input ('Ingrese el valor de costo: '))
        impuesto=0
        if clave==1:
            impuesto=costo*0.1
            categoria1=categoria1+impuesto
        if clave==2:
            impuesto=costo*0.07
            categoria2=categoria2+impuesto
        if clave==3:
            impuesto=costo*0.05
            categoria3=categoria3+impuesto
        impuestoapagar=impuestoapagar+impuesto
        print ('Valor de impuesto: ' + repr (impuesto))
        print ()
    print ('Valor de categoria 1: ' + repr (categoria1))
    print ('Valor de categoria 2: ' + repr (categoria2))
    print ('Valor de categoria 3: ' + repr (categoria3))
    print ('Valor de impuesto a pagar: ' + repr (impuestoapagar))
impuestoautomovilesEDCHP()