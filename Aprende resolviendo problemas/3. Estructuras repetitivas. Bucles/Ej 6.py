# Escribe un programa que muestre la siguiente figura:
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2 
# 1


for x in range(9, 0, -1):
    for y in range(1, x + 1):
        print(y,end= " ")
    print("\n")


