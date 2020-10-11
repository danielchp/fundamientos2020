def  calcularCostoPolizaDMP ():
    #Datos de entrada
    str
puntos=int(input("Digite el valor de puntos:"))
salario=int(input("Digite el valor de calario mini:"))
#proceso
if puntos>=0 and puntos<=100 :
 monto=salario*0.1
else :
 puntos>=101 and puntos<=150 
monto=salario*0.5
if puntos>=151 :
  monto=salario*0.8 
print("El monto del bono del profesor es :",monto)