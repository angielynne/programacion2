from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, nombre_cargo, salario, jefe_inmediato, años_experiencia):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self._nombre_cargo = nombre_cargo
        self._salario = salario
        self._jefe_inmediato = jefe_inmediato
        self._años_experiencia = años_experiencia

    # Getters
    def get_nombre_cargo(self):
        return self._nombre_cargo

    def get_salario(self):
        return self._salario

    def get_jefe_inmediato(self):
        return self._jefe_inmediato

    def get_años_experiencia(self):
        return self._años_experiencia

    # Setters
    def set_nombre_cargo(self, nombre_cargo):
        self._nombre_cargo = nombre_cargo

    def set_salario(self, salario):
        self._salario = salario

    def set_jefe_inmediato(self, jefe_inmediato):
        self._jefe_inmediato = jefe_inmediato

    def set_años_experiencia(self, años_experiencia):
        self._años_experiencia = años_experiencia

    def calcular_cargo(self):
        if self._salario >= 5000000 and self._años_experiencia >= 5 and 25 <= self._edad <= 45:
            self._nombre_cargo = "Senior"
        elif 900000 <= self._salario <= 1200000 and 1 <= self._años_experiencia <= 2 and 18 <= self._edad <= 22:
            self._nombre_cargo = "Junior"
        else:
            self._nombre_cargo = "No clasificado"
