print("Actividad 18")

class Categoria:
    def __init__(self, IDcategoria, nombre):
        self.IDcategoria = IDcategoria
        self.nombre = nombre

class Producto:
    def __init__(self, IDproducto, nombre, precio, IDcategoria, total_compras=0, total_ventas=0, stock=0):
        self.IDproducto = IDproducto
        self.nombre = nombre
        self.precio = precio
        self.IDcategoria = IDcategoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class Gestion_prodcutos:
    def __init__(self):
        self.categorias = {}
        self.productos = {}

    def agregar_categoria(self, IDcategoria, nombre_categoria):
        self.categorias[IDcategoria] = Categoria(IDcategoria, nombre_categoria)
        print("Categoria agregada con éxito")

    def agregar_producto(self, id_producto, nombre_producto, precio, id_categoria, stock):
        self.productos[id_producto] = Producto(id_producto, nombre_producto, precio, id_categoria, stock)
        print("Producto ingresado con éxito... ")

gestion = Gestion_prodcutos()

class Clientes:
    def __init__(self, nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente):
        self.nit_cliente = nit_cliente
        self.nombre_cliente =nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.tel_cliente = tel_cliente
        self.correo_cliente = correo_cliente

class GestionClientes:
    def __init__(self):
        self.diccionario_clientes = {}

    def crear_cliete(self):
        pass

class MenuPricipal:
    def pedir_enteto(self, mensaje):
        while True:
            try:
                return  int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_principal(self):
        opcion = 0
        while opcion !=5:
            print("Menu General")
            print("1. Gestion de productos")
            print("2. Gestion de clientes")
            print("3. Gestion de empleados")

            opcion = self.pedir_enteto("Ingrese su opción: ")
            match opcion:
                case 1:
                    menu_productos.mostrar_menu_produtos()
                case 2:
                    pass





class MenuGestionProductos:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_produtos(self):
        opcion = 0
        while opcion != 5:
            print("MENU")
            print("1. Agregar categoria")
            print("2. Agregar producto")
            print("3. Mostar lista de categotias")
            print("4. Mostrar lista de productos")
            print("5. Salir")
            opcion = self.pedir_entero("Ingrse su opción: ")
            match opcion:
                case 1:
                    id_categoria = input("Ingrse el ID de la categoria: ")
                    nombre_categoria = input("Ingrse el nombre de la categoria: ")
                    gestion.agregar_categoria(id_categoria, nombre_categoria)

                case 2:
                    id_producto = input("Ingrese el ID del producto: ")
                    nombre_producto = input("Ingrese el nombre del producto: ")
                    precio_producto = float(input("Ingrese el precio del producto: Q"))
                    id_cat = input("Ingrese el ID de la categoria: ")
                    if id_cat not in gestion.categorias:
                        print("ERROR, primero agrege la categoria del producto...")
                    else:
                        stock = int(input("Ingrese el stock inicial: "))
                        gestion.agregar_producto(id_producto, nombre_producto, precio_producto, id_cat, stock=stock)

menu_productos = MenuGestionProductos()
