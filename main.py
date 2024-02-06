import Menu
import alumnos
import Profesor


def main():
    while True:
        respuesta = Menu.menu_principal()
        if respuesta == 1:
            respuesta_2 = Menu.menu_registro()
            if respuesta_2 == 1:
                resp1, resp2, resp3, resp4, resp5 = alumnos.preguntas_agre()
                alumno_1 = alumnos.Alumno(resp1, resp2, resp3, resp4, resp5)
                print('Se ha regitrado exitosamente al Alumno.\nTu ID es:')
                print(alumno_1.get_id())
            elif respuesta_2 == 2:
                resp1, resp2, resp3, resp4, resp5 = Profesor.preguntas_agre()
                profesor_1 = Profesor.Profesor(resp1, resp2, resp3, resp4, resp5)
                print('Se ha regitrado exitosamente al Profesor.\nTu ID es:')
                print(profesor_1.get_id())
            else:
                print('¿Seguro quieres salir?'.capitalize())
                respuesta_3 = input('Si/No').upper()
                if respuesta_3 == 'SI':
                    break
                else:
                    continue
        elif respuesta == 2:
            print('Aun no tenemos esa opcion.')
        else:
            print('¿Seguro quieres salir?'.capitalize())
            respuesta_3 = input('Si/No\n').upper()
            if respuesta_3 == 'SI':
                break
            else:
                continue


main()
