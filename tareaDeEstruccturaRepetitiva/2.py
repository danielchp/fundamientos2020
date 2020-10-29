def PrecioDeAmburguesasEDCHP():
    sencilla=int(input("cuantas hamburguesa Sencilla quieres?"))
    doble=int(input("cuantas hamburguesa dobles quieres? "))
    triple=int(input("cuantas hamburguesa triples quieres? "))
    precioSencilla=20
    precioDoble=25 
    precioTriple=28
    if sencilla  <=0:
        print ("no hay pedido de hamburguesas sencillas")
    else:
        if sencilla >=1:
            print(f"el precio de la hamburguesa Sencilla es :{precioSencilla*sencilla}")

    if doble <=0:
        print("no hay pedido de hamburguesas dobles" )
    else:
        if doble >=1:
            print(f"el precio de la hamburguesa doble es :{precioDoble*doble }")
    if triple <=0:
        print("no hay pedido de hamburguesas triples "  )

    else:
        if triple >=1:
            print(f"el costo es hamburguesa Triples {precioTriple*triple}")
    pago = precioSencilla*sencilla + precioDoble*doble + precioTriple*triple 
    tarjeta=pago*0.05
    print("el cargo de la tarjeta es ",tarjeta)
    print("el total a pagar es ",pago + tarjeta)
PrecioDeAmburguesasEDCHP()