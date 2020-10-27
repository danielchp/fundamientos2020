sueldo=int(input("ingrear sueldo"))
interes=0
r=1
for r in range(12) :
   interes=sueldo*0.02
   sueldo=sueldo+interes
   print(f"los años son  {r}  sueldo es   {sueldo}")