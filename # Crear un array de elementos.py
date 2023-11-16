# Crear un array de elementos
elementos = ['manzana', 'banana', 'uva', 'naranja']

# Asignar valores numéricos a cada elemento
valores_numericos = {elemento: i for i, elemento in enumerate(elementos)}

# Imprimir los valores asignados
print("Valores numéricos:", valores_numericos)

# Buscar un elemento por su valor numérico
valor_buscado = 2
elemento_buscado = next((elemento for elemento, valor in valores_numericos.items() if valor == valor_buscado), None)

if elemento_buscado is not None:
    print(f"El elemento con valor numérico {valor_buscado} es: {elemento_buscado}")
else:
    print(f"No se encontró un elemento con valor numérico {valor_buscado}")

#------------------------------------------------------------------------------------------------------------------

palabra_buscada = 'uva'
valor_asociado = valores_numericos.get(palabra_buscada)

if valor_asociado is not None:
    print(f"La palabra '{palabra_buscada}' tiene el valor numérico: {valor_asociado}")
else:
    print(f"No se encontró la palabra '{palabra_buscada}' en el diccionario")