# Escriba una función controlMay(frase) que tome una frase como parámetro y 
# compruebe si dicha frase contiene al menos una letra mayusucal. Si es así, la
# función debe devolver True en caso contratio False.

def controlMay(frase):
    i = 0
    for f in frase:
        if f.isupper():
           i += 1
    if i > 0:
        return True
    else:
        return False
    
print(controlMay("Las verduras son buenas para la salud"))
print(controlMay("estoy aprendiendo el lenguaje de python"))

# or

def controlMay(frase):
   
    for f in frase:
        if f.isupper():
            return True
    return False
   
    
print(controlMay("Las verduras son buenas para la salud"))
print(controlMay("estoy aprendiendo el lenguaje de python"))
