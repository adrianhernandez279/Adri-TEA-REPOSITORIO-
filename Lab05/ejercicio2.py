# Tendencias e Innovacion en Tecnologia Agricola (TEA)
try:
    entrada = input("Ingrese nombre del arcivo: ")
    archivo = open(entrada,"r", encoding="UTF=8")
    for linea in archivo:
        print(linea.upper())
except:
    print("Error archico no existe")


#print(archivo.read())