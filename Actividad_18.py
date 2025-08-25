print("Actividad 18")

class Categoria:
    def __init__(self, IDcategoria, nombre_categoria):
        self.IDcategoria = IDcategoria
        self.nombre_categoria = nombre_categoria

class Producto:
    def __init__(self, IDproducto, nombre_producto, precio, IDcategoria, total_compras=0, total_ventas=0, stock=0):
        self.IDproducto = IDproducto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.IDcategoria = IDcategoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class GestionProductos:
    def __init__(self):
        self.categorias = {}
        self.productos = {}

    def agregar_categoria(self, IDcategoria, nombre_categoria):
        self.categorias[IDcategoria] = Categoria(IDcategoria, nombre_categoria)
        print("Categoria agregada con éxito")

    def agregar_producto(self, id_producto, nombre_producto, precio, id_categoria, stock):
        self.productos[id_producto] = Producto(id_producto, nombre_producto, precio, id_categoria, stock=stock)
        print("Producto ingresado con éxito... ")

    def buscar_producto_por_IDproducto(self, IDbuscado):
        lista = list(self.productos.values())
        for i in range(len(lista)):
            if lista[i].IDproducto == IDbuscado:
                return  lista[i]
        return  None

    def eliminar_producto(self, IDbuscado):
        if IDbuscado in self.productos:
            print(f"¿Seguro que quiere eliminar el producto {IDbuscado}?")
            while True:
                try:
                    confirmacion = int(input("Presione 1 para confirmar la eliminación\nPresione 2 para cancelar: "))
                    if confirmacion == 1:
                        del self.productos[IDbuscado]
                        print(f"Producto con la ID: {IDbuscado} se ha eliminado con éxito.")
                        break
                    elif confirmacion == 2:
                        print("El producto no se eliminó. ;)")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente...")
                except ValueError:
                    print("Error: ingrese un número válido.")
        else:
            print(f"No se encontró ningún producto con ID {IDbuscado}.")


gestion = GestionProductos()

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

    def crear_cliente(self):
        pass

class MenuPrincipal:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return  int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_principal(self):
        opcion = 0
        while opcion !=5:
            print("+++Menu General+++")
            print("1. Gestion de productos")
            print("2. Gestion de clientes")
            print("3. Gestion de empleados")

            opcion = self.pedir_entero("Ingrese su opción: ")
            match opcion:
                case 1:
                    menu_productos.mostrar_menu_productos()
                case 2:
                    pass




class MenuGestionProductos:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_productos(self):
        opcion = 0
        while opcion != 7:
            print("+++ MENU GESTION DE PRODUCTOS +++")
            print("1. Agregar categorias de productos")
            print("2. Agregar producto")
            print("3. Mostar lista de categorias")
            print("4. Mostrar lista de productos")
            print("5. Buscar producto por codigo")
            print("6. Eliminar productos")
            print("7. Salir del menu gestion de productos ")
            opcion = self.pedir_entero("Ingrse su opción: ")
            match opcion:
                case 1:
                    id_categoria = input("Ingrese el ID de la categoria: ")
                    nombre_categoria = input("Ingrese el nombre de la categoria: ")
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
                case 3:
                    if not gestion.categorias:
                        print("No hay categorias registradas... ")
                    else:
                        print("-----LISTA DE CATEGORIAS-----")
                        cont = 1
                        for cat in gestion.categorias.values():
                            print(f"{cont}- ID de categoria: {cat.IDcategoria}, Nombre de categoria: {cat.nombre_categoria}")
                            cont +=1
                case 4:
                    if not gestion.productos:
                        print("No hay productos ingresados... ")
                    else:
                        print("-----LISTA DE PRODUCTOS POR CATEGORIA------")
                        for cat in gestion.categorias.values():
                            print(f"\n>> Categoría: {cat.nombre_categoria} ({cat.IDcategoria})")
                            encontrados = False
                            for p in gestion.productos.values():
                                if p.IDcategoria == cat.IDcategoria:
                                    print(f"   - [{p.IDproducto}] {p.nombre_producto} | Precio: Q{p.precio} | Stock: {p.stock}")
                                    encontrados = True
                        if not encontrados:
                            print("No hay productos en esta categoria... ")
                case 5:
                    print("------BUSCAR PRODUCTO POR CODIGO-----")
                    buscar_codigo = input("Ingrese el codigo que desea buscar: ")
                    encontrado =  gestion.buscar_producto_por_IDproducto(buscar_codigo)
                    if encontrado:
                        print(f"Producto encontrado: {encontrado.IDproducto} |Nombre del producto: {encontrado.nombre_producto} | Precio: {encontrado.precio} | Stock: {encontrado.stock} ")
                    else:
                        print("Producto no encontrado... ")


menu_productos = MenuGestionProductos()
menu_principal = MenuPrincipal()
menu_principal.mostrar_menu_principal()
