def AhorroEDCHP(dias):

    while dias>0:
        ahorro=((dias*(dias+1))/2)**2
    ahorro=ahorro*1
    print(f"lo ahorrado sera de {ahorro} en total")
AhorroEDCHP(365)