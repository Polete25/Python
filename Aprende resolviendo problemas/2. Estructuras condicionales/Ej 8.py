# Escribe un programa que calcule la cantidad neta de acuerdo con los siguientes
# criterios. 

importe = int(input("Introduce un importe: "))
if importe > 1000:
    neto = importe * 0.6
    print(f"Importe neto: {neto}")

elif importe > 100 and importe <= 1000:
    neto = importe * 0.85
    print(f"Importe neto: {neto}")

else:
    neto = importe * 0.95
    print(f"Importe neto: {neto}")
         
