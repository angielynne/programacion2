class Persona:
    def __init__(self, nombre, apellido, direccion, telefono, edad, email):
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono
        self._edad = edad
        self._email = email

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_direccion(self):
        return self._direccion

    def get_telefono(self):
        return self._telefono

    def get_edad(self):
        return self._edad

    def get_email(self):
        return self._email

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_direccion(self, direccion):
        self._direccion = direccion

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_edad(self, edad):
        self._edad = edad

    def set_email(self, email):
        self._email = email