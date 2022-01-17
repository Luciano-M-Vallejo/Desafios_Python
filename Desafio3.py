
# 1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.


# input_1 = int(input('Ingresa el primer numero: '))
# input_2 = int(input('Ingresa el segundo numero: '))
# opciones = ['Sumar', 'Restar', 'Multiplicar', 'Salir' ]

# for i, op in enumerate(opciones):
#     print(i+1, op)
# activar = True
# while activar:
#     input_3 = int(input('Elija una Opcion: '))
#     if input_3 == 1:
#         print( input_1 + input_2)
#     elif input_3 == 2:
#         print( input_1 - input_2)
#     elif input_3 == 3:
#         print( input_1 * input_2)
#     elif input_3 == 4:
#         break
#     elif input_3 != len(opciones):
#         print('La opcion no es correcta')
# else:
#     print('fin del programa')

# 2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

# activar = True
# while activar:
#     input_1 = int(input('Introdusca un numero Impar: '))
#     if input_1%2 == 0:
#         print('Numero incorrecto')
#     else:
#         print('Numero correcto')
#         break
# else:
#     print('fin del programa')

# 3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

# lista = []
# for impar in range(101):
#     if impar%2 == 0:
#         continue
#     else:
#         print(lista)
#         lista.append(impar)

# print(sum(lista))

# 4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

input_numeros = int(input('Cuantos numeros desea introducir: '))
activar = True
lista = []

while activar:
    if len(lista) < input_numeros:
        input_numero = int(input('introduzca su numero: '))
        lista.append(input_numero)
    elif len(lista) >= input_numeros:
        activar= False

medida_A = sum(lista)/len(lista)  
print('Tu medida Aritmética es: ' + str(medida_A))



# 5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# activado = True
# while activado:
#     input_1 = int(input('Introduce un numero del 0 al 9: '))
#     for n in lista:
#         if n == input_1:
#             print('Tu numero es el: ' + str(input_1))
#             activado = False
#             break
# else:
#     print('fin del programa')


# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

# # Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# lista1 = []
# for n in range(0,11):
#     lista1.append(n)
# print(lista1)

# # Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# lista2 = []
# for n in range(-10,1):
#     lista2.append(n)
# print(lista2)

# # Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# lista3 = []
# for n in range(0,21):
#     if n%2 == 0:
#         lista3.append(n)
# print(lista3)

# # Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# lista4 = []
# for n in range(-20,1):
#     if n%2 != 0:
#         lista4.append(n)
# print(lista4)

# # Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# lista5 = []
# for n in range(0,51):
#     if n%5 == 0:
#         lista5.append(n)
# print(lista5)


# 6) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
# lista_3 = []
# lista_4 = []

# for l1 in lista_1:
#     for l2 in lista_2:
#         if l1 == l2:
#             lista_3.append(l2)
# for l3 in lista_3:
#     if l3 not in lista_4:
#         lista_4.append(l3)

# print(lista_4)