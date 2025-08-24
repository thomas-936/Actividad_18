print("Actividad 18")

class Categoria:
    def __init__(self, IDcategoria, nombre):
        self.IDcategoria = IDcategoria
        self.nombre = nombre

class Producto:
    def __init__(self, IDproducto, nombre, precio, IDcategoria, total_compras, total_ventas, stock):
        self.IDproducto = IDproducto
        self.nombre = nombre
        self.precio = precio
        self.IDcategoroia = IDcategoria
        self.total_compras = total_compras
        self.total_vetas = total_ventas
        self.stock = stock

