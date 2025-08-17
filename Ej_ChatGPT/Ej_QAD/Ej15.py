# Escribe una función que reciba un número entero y devuelva ese 
# número con sus dígitos invertidos, utilizando únicamente operaciones
# matemáticas (sin convertirlo en cadena).


def invertir_num(num: int) -> int:
        invertido = 0
        while num > 0:
            digito = num % 10
            invertido = invertido * 10 + digito
            num = num // 10

        return invertido

 