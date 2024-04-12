# README
## Contador de vocales

### Autor

Carlos Emmanuel Denis

### Descripción

Este script de Python define una función `cont_vocales(string)` que cuenta el número de veces que aparecen las vocales en una cadena de texto. La función es útil para análisis de texto y aplicaciones educativas donde se requiere identificar la frecuencia de vocales.

### Cómo Funciona

La función `cont_vocales(string)` recibe como argumento una cadena de texto (`string`). Retorna un diccionario donde las claves son las vocales y los valores son las cantidades de veces que cada vocal aparece en el texto.

El algoritmo funciona de la siguiente manera:

1. Utiliza la librería `unidecode` para eliminar diacríticos de las letras (por ejemplo, convertir "é" a "e").
2. Convierte la cadena de texto a minúsculas para asegurar que el conteo de vocales sea insensible a mayúsculas.
3. Itera sobre cada letra de la cadena. Si la letra es una vocal, incrementa el contador correspondiente en el diccionario de resultados.
4. Si una vocal no está presente en la cadena, no aparecerá en el diccionario de resultados.

### Uso

Aquí hay un ejemplo de cómo usar la función `cont_vocales`:

```python
texto = "Hola, ¿cómo estás?"
resultado = cont_vocales(texto)
print(resultado)
```

> Este código imprimirá el conteo de cada vocal en la cadena "Hola, ¿cómo estás?", mostrando cuántas veces aparece cada una. Por ejemplo: {'a': 2, 'e': 1, 'o': 2}

### Requisitos

- Python 3.11.2
- Libreria Unidecode

Para instalar Unidecode, puedes utilizar pip:

	pip install unidecode