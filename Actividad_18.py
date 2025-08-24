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


class Gestion_prodcutos:
    def __init__(self):
        self.categoria = {}
        self.producto = {}

    def agragar_categoria(self, IDcategoria, nombre_categoria):
        self.categoria[IDcategoria] = Categoria(IDcategoria, nombre_categoria)
        print("Categoria agregada con éxito")

gestion = Gestion_prodcutos()

class Menu:

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar(self):
        opcion = 0
        while opcion != 5:
            print("MENU")
            print("1. Agregar categoria")
            print("2. Agregar producto")
            print("3. Mostar lista de categotias")
            print("4. Mostrar lista de productos")
            opcion = self.pedir_entero("Ingrse su opción")
            match opcion:
                case 1:
                    id_categoria = input("Ingrse el ID de la categoria: ")
                    nombre_categoria = input("Ingrse el nombre de la categoria: ")
                    gestion.agragar_categoria(id_categoria, nombre_categoria)