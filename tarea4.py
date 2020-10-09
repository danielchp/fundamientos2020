hora =int(input("ingrese el numero de horas :"))

if hora<=2 :
    cobro = hora*5*1
else :
    hora>=3 and hora<6 
    cobro=hora*4*1

    if hora>5 and hora>11 :
        cobro=hora*3*1*1
    else :
         hora>10 
         cobro=hora*2*1*1*1
print("el precio total es:",cobro)
         


