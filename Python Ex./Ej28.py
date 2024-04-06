# Escriba un programa que permita calcular el timepo de ejecución de un script.
# Tomemos como ejemplo el scrip del ejercicio 24 y calculemos su timepo de 
# ejecución. El programa debe mostrar al final la tabla de multiplicación del 
# ejercicio 24 junto con el tiempo de ejecución.

import time

inicio = time.time()

for i in range(0,11):
    v = 8 * i
    print(f"8 x {i} = {v}")
    
final = time.time()

print("Tiempo de ejecución del código: ", final - inicio)