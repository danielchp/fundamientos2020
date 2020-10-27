nombre1=bool(input("ingrese su nombre:"))
nombre2=bool(input("ingrese su nombre:"))
nombre3=bool(input("ingrese su nombre:"))
edad1=int(input("ingrese su edad:"))
edad2=int(input("ingrese su edad:"))
edad3=int(input("ingrese su edad:"))
if edad1<edad2 and edad1<edad3 :
    print("el nombre y la edad de la persona es:",nombre1 ,edad1)
if edad2<edad3 :
    print("el nombre y la edad de la persona es:",nombre2 ,edad2)
else :
    print("el nombre y la edad de la persona es:",nombre3 ,edad3)