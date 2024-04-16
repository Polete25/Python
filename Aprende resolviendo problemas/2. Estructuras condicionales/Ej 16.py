# ¿Podría averiguar cuál es el resultado esperado después de ejecutrar el 
# siguiente programa?

x = 86 
y = -99

if x % 2 == 0:
    x = y
    y = y * 2
else:
    y = x / 2
    x = x * 2

print(x, y)

