def ahorrosEDCHP():
  años=int(input("ingrear años transcurridos"))
   interes=0
   r=1
  for r in range(años) :
      interes=1500*0.15
      sueldo=1500+interes
      
  print(f"los años son  {r}  sueldo es   {sueldo}")
ahorrosEDCHP()