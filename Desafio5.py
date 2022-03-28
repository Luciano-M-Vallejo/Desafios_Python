# 1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura

area = ''
def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

area = area_rectangulo(15, 10)

print(area)

# 2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio

import math

area = ''

def area_circulo(radio):
    resultado = (radio **2) * math.pi
    return resultado

area = area_circulo(5)
print(area)

# 3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

resultado = ''
def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    elif a == b:
        return 0

resultado = relacion(5, 10)
print(resultado)
resultado = relacion(10, 5)
print(resultado)
resultado = relacion(5, 5)
print(resultado)

# 4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
# Comprueba el punto intermedio entre -12 y 24

inter = ''
def intermedio(a, b):
    resultado = (a + b) / 2
    return resultado

inter = intermedio(-12, 24)
print(inter)

# 5) Realizá una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(nrecortar, linferior = 0, lsuperior = 10):
    if nrecortar < linferior:
        return f'El limite inferior es {linferior}'
    elif nrecortar > lsuperior:
        return f'El limite superior es {lsuperior}'
    else:
        return nrecortar

resultado = recortar(15)
print(resultado)

# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

# pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]

lista = [6,5,2,1,7]
def separar(param):
    pares = []
    impares = []
    for l in param:
        if l % 2 == 0:
            pares.append(l)
            pares.sort()
        else:
            impares.append(l)
            impares.sort()
    return pares, impares

pares, impares = separar(lista)
print(pares)
print(impares)
