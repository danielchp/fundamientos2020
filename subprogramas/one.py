class Subprograma:
    def factorial(self,numero):
        contador=1
        if numero==0:
            resultado=1
        else :
            resultado=numero
        while contador<numero:
            resultado=resultado*contador
            contador=contador+1
        print(f"El factor de{numero} es {resultado}")
        
    def rangofactorial(self,numfinal):
        for inicio in range(numfinal+1):
            self.factorial(inicio)
obj=Subprograma()
obj.rangofactorial(26)