# Escribe un programa que reciba la calificación del usuario y muestre la 
# califcación de acuerdo con los siguientes criterios.

nota = int(input("Introduzca su nota: "))

if nota > 95:
    print("Tu calificación es A+")
elif nota > 90 and nota <= 95:
    print("Tu calificación es A")
elif nota > 80 and nota <= 90:
    print("Tu calificación es B")
elif nota >= 60 and nota <= 80:
    print("Tu calificación es C")
elif nota < 60:
    print("Tu calificación es D")
    
    