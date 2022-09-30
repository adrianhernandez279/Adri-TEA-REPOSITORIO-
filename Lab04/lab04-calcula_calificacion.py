# Tendencias e Innovacion en Tecnologia Agricola (TEA)

def imprimirCalif(Calificacion):
    if(Puntuacion >= 0.9 and Puntuacion <=1.0):
        Calificacion = "sobresaliete"
    elif(Puntuacion >= 0.8 and Puntuacion <0.9):
        Calificacion = "notable"
    elif(Puntuacion >= 0.7 and Puntuacion <0.8):
        Calificacion = "bien"
    elif(Puntuacion >= 0.6 and Puntuacion < 0.7):
        Calificacion = "suficiente"
    elif(Puntuacion >= 0 and Puntuacion <0.6):
        Calificacion = "Insuficiente"
    else: 
        Calificacion = "Puntuacion Incorrecta" 
    return Calificacion 

try:
    Puntuacion = float(input("Ingrese la puntuacion con valores entre 0.01 y 1.00:"))
    Calificacion = imprimirCalif(Puntuacion)
    print("La calificacion de su puntuacion es: ", Calificacion)
except:
    print("Error, puntuacion solamente acepta numeros")