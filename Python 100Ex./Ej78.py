# Escriba una función split(frase,caracter) que convierta una sentencia en una 
# lista utilizando el separador de caracteres. 

def split(frase,caracter):
    frase_lista = list()
    palabra_tmp = str()
    if caracter in frase:
        for i in range(len(frase)):
            if frase[i] != caracter:
                palabra_tmp += frase[i]
                if i == len(frase-1):
                    frase_lista += [palabra_tmp]
            else:
                frase_lista += [palabra_tmp]
                palabra_tmp = ""
                
        return frase_lista
    else:
        frase_lista += [frase]
        return frase_lista
    
