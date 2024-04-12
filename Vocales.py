import unicodedata


def cont_vocales(string):
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    string_lower = string.lower()
    string_normalizado = unicodedata.normalize('NFKD', string_lower)
    string_final = ''.join([c for c in string_normalizado if not unicodedata.combining(c)])

    print("Palabras" + " = " + string)

    for letra in string_final:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    print("Total de vocales =", sum(resultado.values()))
    return resultado

def inputPalabras():
    print("Escriba '1' para ingresar una palabra o '0' para seguir")
    sino = input()

    if sino == '1':
        print("Ingrese una palabra.")
        text = input()
        cont_vocales(text)
    elif sino == '0':
        print("No se ingresó texto.")
    else:
        print("Opción no válida.")

inputPalabras()