# algoritno para bono navideño
sueldo=int(input("ingreasr sueldo"))
año=int(input("introducir años trabajado"))
if sueldo <2000 and año<4 :
    sueldof=sueldo+((sueldo*25)/100)
else :
    sueldof=sueldo+((sueldo*20)/100)
    print ("su bono sera",sueldof)