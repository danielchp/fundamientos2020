precio=int(input("ingrese el costo:"))
if precio<=200 :
    descuentox=(precio*15)/100
    pagofinalx=precio-descuentox
    if precio<=100>200 :
     descuentoy=(precio*12)/100
     pagofinaly=precio-descuentoy
    else :
     descuentoz=(precio*10)/100
    pagofinalz=precio-descuentoz
    print("total a pagar",pagofinalz)