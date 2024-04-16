# Escribe un programa que muestre la siguiente pirámide de estrellas:
# *
# **
# ****
# *******
# *********

for i in range(1,11):
    if i == 1 or i%2 == 0:
        print('*'*i)
