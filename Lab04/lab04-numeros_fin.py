# Tendencias e Innovacion en Tecnologia Agricola (TEA)
contador = 0
suma = 0
minimo = 0
maximo = 0
primerNum = True 
while True:
    try:
        numero = input("Ingrese un numero: ")
        if (numero == "salir"):
            print("suma", suma)
            print("promedio", suma/contador)
            print("contador", contador)
            break
        contador = contador +1
        suma=suma + int(numero)
        if (primerNum):
            minimo= int(numero)
            maximo= minimo
            primerNum= False
        else:
            if(int(numero)>maximo):
                maximo= int(numero)
            if(int(numero)<minimo):
                minimo= int(numero)
            print("contador", contador)
    except:
        print("Entrada invalda")
            
