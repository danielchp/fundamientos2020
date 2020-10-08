horas=int(input("cuanto tiempo trabajo por dia"))
sueldo=int(input("cuanto le pagan por hora"))
horasS=horas*7
if horasS<=40 :
       horax=horasS-40
       sueldoF=(horasS*sueldo)+(horax*sueldo)
       print("tu pago semanal es")
else:
    sueldoF=(horasS*sueldo)
    print(" tu sueldo es de")