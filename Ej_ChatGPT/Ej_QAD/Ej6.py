# Escribe una función que invierta un string sin usar [::-1].

def invertir_string(string: str) -> str:
    gnirts = ''
    for s in string:
        gnirts = s + gnirts   
    return gnirts

print(invertir_string('Python'))