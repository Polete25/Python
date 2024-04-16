# El número palindrómo más grande obtenido como producto de dos números de dos 
# dígitos es 9009 = 91 x 99. Escribir un programa que encuentre el número
# palindrómico más grande obtenido como producto de dos número de tres dígitos.
# Nota: Puede usar la función esUnPalindromo del ejercicio anteriro.


def isdigit(numero):
    numero = str(numero)
    left = 0
    right = len(numero) - 1
    
    while left < right:
        if numero[left] != numero[right]:
            return False
        left += 1
        right -= 1
    return True

n1 = int()
n2 = int()
pal = list()
for n1 in range(100,1000):
    for n2 in range (100,1000):
        p = n1 * n2
        if isdigit(p):
            pal.append(p)
            
print(max(pal))
