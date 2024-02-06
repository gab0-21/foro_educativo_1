import os
import time


def isdigit(argumento):
    while True:
        if argumento.isdigit():
            argumento = int(argumento)
            break
        else:

            print('No es valido.')
            continue
    return argumento


def menu_principal():
    os.system('cls')
    print('Menu Principal'.center(50, ' '))
    print('1.- Registrarte. ')
    print('2.- Iniciar sesión.')
    print('3.- Salir.')
    while True:
        respuesta = input('Ingresa a respuesta por el numero:\n')
        respuesta = isdigit(respuesta)
        if respuesta <= 3:
            break
        else:
            print('No es valido.')
            time.sleep(1)
            continue
    return respuesta


def menu_registro():
    print('Menu de Registro.'.center(50, ' '))
    print('1.- Alumno\n2.- Profesor\n3.- Salir.')
    while True:
        respuesta = input('Ingresa a respuesta por el numero:\n')
        respuesta = isdigit(respuesta)
        if respuesta <= 3:
            break
        else:
            print('No es valido.')
            time.sleep(1)
            continue
    return respuesta

