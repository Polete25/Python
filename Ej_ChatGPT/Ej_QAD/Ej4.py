# Comprobar si dos palabras son anagramas (tienen las mismas letras en distinto orden).

def son_anagramas(pala1: str, pala2: str) -> bool:
    n = 0
    for pal1 in pala1:
        for pal2 in pala2:
            if pal1 == pal2:
                n = n+1
                break

    if len(pala1) == n:
        m = 0
        for pal2 in pala2:
            for pal1 in pala1:
                if pal1 == pal2:
                    m = m + 1
                    break

        if len(pala2) == m:
            return True
        else: 
            return False
    else:
        return False

print(son_anagramas("roma", "amor"))  # True
print(son_anagramas("python", "typhon"))  # True
print(son_anagramas("data", "date"))  # False