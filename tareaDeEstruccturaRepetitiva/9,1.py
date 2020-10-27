def presioDeAmburguesa():
    str
S=int(input("ingresar 1 si es una amburgesa simple, 2 si es doble y 3 si es triples:"))
N=int(input("cuantas amburguesas  quieres:"))

if S==1 :
     precioI=20*N
     precioF=precioI+((precioI*5)/100)
     if S==2:
         precioId=25*N
     precioF=precioI+((precioI*5)/100)
else :
         S==3
         precioI=29*N
         precioF=precioI+((precioI*5)/100)
      
   
print(F"el monto a pagr es: {precioF} soles")
presioDeAmburguesa()