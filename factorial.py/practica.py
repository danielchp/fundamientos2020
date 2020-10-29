años=int(input("ingrear sueldo"))
interes=0
dinero=1500
r=1
for r in range(años) :
   interes=dinero*0.15
   dinero=dinero+interes
print(f"sueldo es   {dinero}")