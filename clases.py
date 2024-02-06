class Clase:
    def __init__(self, nombre, profesor, horario, codigo):
        self.__nombre = nombre.upper()
        self.__profesor = profesor.upper()
        self.__horario = horario
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def get_profesor(self):
        return self.__profesor

    def get_horario(self):
        return self.__horario

    def get_codigo(self):
        return self.__codigo
    