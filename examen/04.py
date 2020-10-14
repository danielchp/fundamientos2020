def definirsigno_correspondiente():
    #datos de entrada
    
    operacion=int(input("ingrsa 1 si es suma, 2 es resta, 3 si es multiplicacion, 4 si es divicion, 5 si es ponencia:"))
    dato1=int(input("ingresa el primer valor"))
    dato2=int(input("ingresar el segundo valor"))
    #proceso
    if operacion<2 and operacion>0:
        suma=dato1+dato2
        
    else:
        operacion<3 and operacion>1
        suma=dato1-dato2
 
    if operacion>2 and operacion<4 :
           suma=dato1*dato2
    elif operacion <5 and operacion>3:
     suma=dato1/dato2
     if operacion<6 and operacion>4 :
         suma=dato1**dato2
    print("el resultado  es:",suma)
definirsigno_correspondiente()