# Escirbe un programa que muestre los siguientes números en la consola:

L = list(range(5,21))
i = 0

while i <  8:
    print(*L, sep=' ')
    i += 1

print("-------")
# or

for i in range(8):
    for j in range(5,21):
        print(j,end = " ")
    
    print()