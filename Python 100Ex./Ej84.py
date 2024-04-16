# Escribir una función codigoSuma(numero) que toma como parámetro un número 
# entero numero estricatmente mayor que 100 y perite determinar un código a 
# partir de ese número, siguiendo los suguientes pasos: Paso1 -> Suma de los 
# dígitos del número introducido en el parámetro. Paso2 -> Repite el cálculo de
# la suma obtenida (en el paso1) siempre que no esté entre 1 y 9. 
# El código será el número pasado como parámetro al que añadimos la última suma
# obtenida a su izquierda.

def codigoSuma(n):
    if n >= 100:
        s = n
        
        while s < 1 or s > 9:
            num = str(s)
            s = 0 
            
            for digito in num:
                s += int(digito)
                
    return str(s) + str(n)
    
print(codigoSuma(69810))
print(codigoSuma(3201))