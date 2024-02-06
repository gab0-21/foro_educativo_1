def preguntas_agre():
    print('Agregar Alumno'.center(50, ' '))
    user_name = input("Ingrese el nombre del Profesor: \n")
    user_last_name = input("Ingrese el apellido del Profesor: \n")
    while True:
        user_edge = input("Ingrese la edad del Profesor: \n")
        if user_edge.isdigit():
            break
        else:
            continue
    user_adress = input("Ingrese el correo del Profesor: \n")
    user_grade = input('Ingresa la cedula del Profesor:\n')
    return user_name, user_last_name, user_edge, user_adress, user_grade


class Profesor:
    def __init__(self, nombre, apellido, edad, correo, cedula):
        self.__nombre = nombre.upper()
        self.__apellido = apellido.upper()
        self.__edad = edad
        self.__correo = correo
        self.__cedula = cedula.upper()
        self.__identificador = self.__nombre[:3] + self.__apellido[:3] + str(self.__edad)
        self.__clases = {}

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_id(self):
        return self.__identificador

    def get_clases(self):
        titulos = []
        for keys in self.__clases:
            titulos.append(keys)
        return ','.join(titulos)

    def agregar_clase(self, clase):
        self.__clases[clase.get_nombre()] = clase

    def eliminar_clase(self, nombre):
        self.__clases.pop(nombre)

    def mostrar_datos_usuario(self):
        titulos = []
        for keys in self.__clases:
            titulos.append(keys)
        cadena = (self.__nombre + ' ' + self.__apellido + '\n' + 'Edad: ' + str(self.__edad) + '\n' + 'Correo: ' +
                  self.__correo + '\n' + 'Id: ' + self.__identificador + '\n' + 'clases:'
                  + ','.join(titulos))
        print(cadena)

