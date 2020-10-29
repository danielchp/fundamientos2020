def promedioEDCHP():
    n = int(input("Ingrese el numero de estudiantes: "))
    m = int(input("Ingrese el numero de salones: "))
    promedio = 0
    suma1 = 0
    for i in range(m):
        suma = 0
        promedio = 0
        for i in range(n):
            edad = int(input("Ingrese la edad"))
            suma = suma + edad
            promedio = suma/n
        print("EL promedio es: ", promedio)
        suma1 = suma1 + promedio
        promediototal = suma1/m
        print("El promedio del colegio es: ", promediototal)
promedioEDCHP()