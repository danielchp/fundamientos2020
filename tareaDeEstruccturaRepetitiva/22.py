def salarioDelClienteEDCHP():
    ganaciaporintereses = 0
    n = int (input ('Ingrese el valor de n: '))
    for i in range (1, n + 1):
        print ('PROCESO ' + repr (i))
        comprasrealizadas = float (input ('Ingrese el valor de compras realizadas: '))
        pagodelcorteanterior = float (input ('Ingrese el valor de pago del corte anterior: '))
        saldoanterior = float (input ('Ingrese el valor de saldo anterior: '))
        if saldoanterior*0.15>pagodelcorteanterior:
            intereses=saldoanterior*0.12
            multa=200
        else:
            intereses=0
            multa=0
        saldoactual=saldoanterior+comprasrealizadas-pagodelcorteanterior+intereses+multa
        pagominimo=saldoactual*0.15
        pagoparanogenerarintereses=saldoactual*0.85
        ganaciaporintereses=ganaciaporintereses+intereses
        print ('Valor de intereses: ' + repr (intereses))
        print ('Valor de multa: ' + repr (multa))
        print ('Valor de pago minimo: ' + repr (pagominimo))
        print ('Valor de pago para no generar intereses: ' + repr (pagoparanogenerarintereses))
        print ('Valor de saldo actual: ' + repr (saldoactual))
    print ('Valor de ganacia por intereses: ' + repr (ganaciaporintereses))
salarioDelClienteEDCHP()