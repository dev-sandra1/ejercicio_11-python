#Comprobar si una Palabra es un Palíndromo
#Un palíndromo es una palabra que 
# se lee igual de izquierda a derecha que de derecha a izquierda, como "radar" o "oso".

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convierte a minúsculas
    palabra_invertida = palabra[::-1]  # Invierte la palabra
    return palabra == palabra_invertida 


print(es_palindromo("Radar"))   
print(es_palindromo("usu"))     
print(es_palindromo("Python"))  # False
