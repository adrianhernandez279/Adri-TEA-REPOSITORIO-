# Tendencias e Innovacion en Tecnologia Agricola (TEA)
def calcularTotal(horas, tarifa):
    horas_ex = horas - MAX_HORAS_SEM
    if(horas_ex > 0):
         total = (MAX_HORAS_SEM * int (tarifa)) + (horas_ex * (int(tarifa)*1.5))
    else:
       total = int(horas) * int(tarifa) 
    return total

try:
    MAX_HORAS_SEM= 40
    horas = input ("Introduzca Horas: ") 
    tarifa = input ("Introduzca Tarifa: ")
    total = calcularTotal(horas, tarifa)
    print ("Salario: " ,total)
except: 
    print ("Error, debe ingresar un valor numerico")