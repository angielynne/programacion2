class Producto:
    def __init__(self, nombre, preunitario, stock): 
        self.nombre = nombre
        self.preunitario = preunitario
        self.stock = stock

productos = [
    Producto("Manzanas", 200, 100),
    Producto("Naranjas", 100, 80),
    Producto("Plátanos", 300, 50)
]