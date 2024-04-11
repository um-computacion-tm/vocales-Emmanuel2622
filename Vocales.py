def cont_vocales(string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    string_lower = string.lower()

    for letra in string_lower:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado