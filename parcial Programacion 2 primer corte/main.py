from empleado import Empleado

def main():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    edad = int(input("Ingrese la edad: "))
    email = input("Ingrese el email: ")
    salario = int(input("Ingrese el salario: "))
    jefe_inmediato = input("Ingrese el nombre del jefe inmediato: ")
    años_experiencia = int(input("Ingrese los años de experiencia: "))

    empleado = Empleado(nombre, apellido, direccion, telefono, edad, email, "", salario, jefe_inmediato, años_experiencia)
    empleado.calcular_cargo()

    print("\nDetalles del Empleado:")
    print(f"Nombre: {empleado.get_nombre()} {empleado.get_apellido()}")
    print(f"Dirección: {empleado.get_direccion()}")
    print(f"Teléfono: {empleado.get_telefono()}")
    print(f"Edad: {empleado.get_edad()}")
    print(f"Email: {empleado.get_email()}")
    print(f"Salario: {empleado.get_salario()}")
    print(f"Jefe Inmediato: {empleado.get_jefe_inmediato()}")
    print(f"Años de Experiencia: {empleado.get_años_experiencia()}")
    print(f"Cargo: {empleado.get_nombre_cargo()}")

if __name__ == "__main__":
    main()
