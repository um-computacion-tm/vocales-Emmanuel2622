import unicodedata

def cont_vocales(string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    string = unicodedata.normalize('NFKD', string)
    string = ''.join([c for c in string if not unicodedata.combining(c)])
    string_lower = string.lower()
    
    print(string)
    for letra in string_lower:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado
