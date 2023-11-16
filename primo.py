def factorizar(n):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if n % numero_primo_actual != 0:
            numero_primo_actual = next(numeros_primos)
            continue
        resultado.append(numero_primo_actual)
        n = cociente = n / numero_primo_actual
    return resultado
v=6

print(factorizar(v))

facto = factorizar(v)

print(len(facto))

for i in range(len(facto)):
    print(facto[i])


"""
n = int(input("Ingrese un número mayor a 1: "))
if n > 1:
    factores = factorizar(n)
    print(f"Factorización de {n}:", " x ".join(map(str, factores)))
else:
    print("Ingrese un número mayor a 1.")"""