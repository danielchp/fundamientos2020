def factorial():
    numero=int(input("ingresar valores"))
    contador=1
    if numero==0:
        resultado=1
    else:
        resultado=numero
    while contador<numero:
        resultado=resultado*contador
        contador=contador+1
    print(f"El factorial del {numero} es{resultado}")
factorial()