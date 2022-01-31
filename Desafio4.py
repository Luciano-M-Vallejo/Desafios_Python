# AÑO BISIESTO

activar = True

def ano_bisiesto(param):
    if param%4 == 0:
        if param%100 != 0:
            print('Es un Año Bisiesto!!!')
        elif param%100 == 0 and param%400 == 0:
            print(f'El año {param} es Bisiesto')
        else:
            print(f'El año {param} NO es Bisiesto')
    else:
        print(f'El año {param} NO es Bisiesto')

while activar:
    try:
        input_ano = int(input('Ingrese un año: '))
        if len(str(input_ano)) == 4:
            ano_bisiesto(input_ano)
            activar = False
        else:
            print('Ingrese un numero de 4 digitos')
    except ValueError:
        print('Solo se permiten numeros')
