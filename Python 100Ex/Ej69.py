# Escribir una función numDiasHoras(fechaInicio,fechaFin) que tome dos 
# parámetros de entrada: la fecha de inicio fechaInicio y la fecha de fin 
# fechaFin. Esta función nos permitirá calcular el número de días y el número de 
# horas entre la fecha de inicio y la fecha de fin pasadas como parámetros. La 
# funicón debe devolcer la tupla(NumDias,NumHoras).

import datetime

def numDiasHoras(fechaInicio,fechaFin):
    fechaInicio = datetime.datetime.strptime(fechaInicio, '%Y/%m/%d')
    fechaFin = datetime.datetime.strptime(fechaFin, '%Y/%m/%d')
    diferencia = fechaFin - fechaInicio
    L1 = list()
    L1.append(diferencia.days)
    L1.append(diferencia.days * 24)
    return L1

print(numDiasHoras("2022/05/15","2022/06/20"))
print(numDiasHoras("2022/04/1","2022/04/27"))
