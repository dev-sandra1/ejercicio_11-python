# Encontrar el Mayor de Tres Números

def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplo de prueba
print(mayor_de_tres(5, 12, 9))
