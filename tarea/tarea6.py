precio=int(input("ingrese el costo:"))
if precio<=200 :
    descuentox=(precio*15)/100
    pagofinal=precio-descuentox
    if precio<=100>200 :
     descuentoy=(precio*12)/100
     pagofinal=precio-descuentoy
    else :
     descuentoz=(precio*10)/100
    pagofinal=precio-descuentoz
print("total a pagar",pagofinal)