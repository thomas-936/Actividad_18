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

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO valido... ")

    def crear_cliente(self, nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente):
        self.diccionario_clientes[nit_cliente] = Clientes(nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente)

    def quicksort_clientes(self, clientes):
        if len(clientes) <= 1:
            return clientes
        pivot = clientes[0]
        menores = [c for c in clientes[1:] if c.nombre_cliente.lower() <= pivot.nombre_cliente.lower()]
        mayores = [c for c in clientes[1:] if c.nombre_cliente.lower() > pivot.nombre_cliente.lower()]
        return self.quicksort_clientes(menores) + [pivot] + self.quicksort_clientes(mayores)

    def buscar_cliente_por_nit(self, busco_nit_cliente):
        lista_clentes = list(self.diccionario_clientes.values())
        for j in range(len(lista_clentes)):
            if lista_clentes[j].nit_cliente == busco_nit_cliente:
                return lista_clentes[j]
        return None

    def modificar_datos_cliente(self, nit):
        if nit in self. diccionario_clientes:
            cliente = self.diccionario_clientes[nit]
            print(f"Cliente econtrado {cliente.nombre_cliente}")
            print("¿Que dato desea modificar?")
            print("1. Correo")
            print("2. Teléfono")
            opcion = gestion_clientes.pedir_entero("Ingrese la Opción que desea modificar: ")

            if opcion == 1:
                nuevo_correo = input("Ingrese el nuevo correo del cliente: ")
                cliente.correo_cliente = nuevo_correo
                print("Correo modificado con éxito... ")
            elif opcion ==  2:
                nuevo_telefono = input("Ingrese el nuevo Teléfono del cliente: ")
                cliente.tel_cliente = nuevo_telefono
                print("Teléfono modificado con éxito... ")

    def eliminar_clientes(self, nit_cliente):
        if nit_cliente in self.diccionario_clientes:
            cliente = self.diccionario_clientes[nit_cliente]
            print(f"¿Seguro que quiere eliminar al cliente {cliente.nombre_cliente} con el NIT: {cliente.nit_cliente}?")
            confirmacion = self.pedir_entero("Ingrese 1 para confirmar o dos para cancelar: ")
            if confirmacion == 1:
                del  self.diccionario_clientes[nit_cliente]
                print("Cliente elimindo con éxito... ")
            else:
                print("Eliminación cancelada")
        else:
            print(f"No se encontro un cliente con el NIT: {nit_cliente}")

gestion_clientes = GestionClientes()

class MenuGestionDeClientes:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_gestion_clientes(self):
        opcion = 0
        while opcion != 6:
            print("+++ MENU GESTION DE CLIENTES+++")
            print("1. Crear nuevo cliente")
            print("2. Mostrar todos los clientes")
            print("3. Buscar clientes")
            print("4. Modificar clientes")
            print("5. Eliminar clientes")
            print("6. Salir del menu")
            opcion = self.pedir_entero("Ingrese su Opción: ")
            match opcion:
                case 1:
                    while True:
                        nit_cliente = input("Ingrese el nit del cliente: ")
                        if nit_cliente in gestion_clientes.diccionario_clientes:
                            print("Este nit ya esta registrado, intente de nuevo... ")
                        else:
                            nombre_cliente = input("Ingrese el nombre del cliente: ")
                            direccion_cliente = input("Ingrese la direccion del cliente: ")
                            tel_cliente = input("Ingrese el número de teléfono del cliente: ")
                            correo_cliente = input("Ingrese el correo del cliente: ")
                            gestion_clientes.crear_cliente(nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente)
                            print("Cliente credo con éxito ;)")
                            break
                case 2:
                    if not gestion_clientes.diccionario_clientes:
                        print("No hay clientes registrados...")
                    else:
                        print("----- LISTA DE CLIENTES ORDENADA -----")
                        lista_clientes = list(gestion_clientes.diccionario_clientes.values())
                        lista_ordenada = gestion_clientes.quicksort_clientes(lista_clientes)
                        for c in lista_ordenada:
                            print(
                                f"NIT: {c.nit_cliente} | Nombre: {c.nombre_cliente} | Dirección: {c.direccion_cliente} | Tel: {c.tel_cliente} | Correo: {c.correo_cliente}")
                case 3:
                    if not gestion_clientes.diccionario_clientes:
                        print("No hay clientes resgistrados... ")
                    else:
                        print("-----BUSCAR CLIENTE POR NIT-----")
                        buscar_nit = input("Ingrese el nit del cliente: ")
                        encontrado = gestion_clientes.buscar_cliente_por_nit(buscar_nit)
                        if encontrado:
                            print(f"El cliente con el NIT {encontrado} es {encontrado.nombre_cliente}")
                        else:
                            print("Cliente no encontrado... ")

                case 4:
                    print("---MODIFFICAR DATOS--- ")
                    nit_cliente_modificar = input("Ingrese el NIT del cliente para buscarlo: ")
                    gestion_clientes.modificar_datos_cliente(nit_cliente_modificar)

                case 5:
                    print("---ELIMINAR CLIENTES---")
                    eliminar = input("Ingrse el NIT del cliente que desea eliminar: ")
                    gestion_clientes.eliminar_clientes(eliminar)


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
                    menu_gestion_clientes.mostrar_menu_gestion_clientes()
                case 3:
                    menu_gestion_empleados.mostrar_menu_empleados()
                case 4:
                    pass


class PuestosDeEmpleado:
    def __init__(self, id_puesto, nombre_puesto):
        self.id_puesto = id_puesto
        self.nombre_puesto = nombre_puesto

class Empleados:
    def __init__(self, id_empledo, nombre, id_puesto, direccion, telefono, correo):
        self.id_empledo = id_empledo
        self.nombre = nombre
        self.IDpuesto = id_puesto
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class GestionEmpleados:
    def __init__(self):
        self.diccionario_puestos_empleados = {}
        self.diccionario_empleados = {}

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO VALIDO... ")

    def agregar_puesto_empleado(self, IDpuesto, nombre_puesto):
        self.diccionario_puestos_empleados[IDpuesto] = PuestosDeEmpleado(IDpuesto, nombre_puesto)
        print("Puesto de empleado agragado con éxito... ")

    def agregar_empleado(self, IDempledo, nombre_empleado, IDpuesto, direccion_empleado, telefono_empleado, correo_empleado):
        self.diccionario_empleados[IDempledo] = Empleados(IDempledo, nombre_empleado, IDpuesto, direccion_empleado, telefono_empleado, correo_empleado)
        print("Empleado agregado con éxtio... ")

    def mostrar_empleados_por_puesto(self):
        if not self.diccionario_empleados:
            print("No hay empleados registrados...")
            return

        print("\n=== EMPLEADOS POR PUESTO ===")
        for id_puesto, puesto in self.diccionario_puestos_empleados.items():
            print(f"\n>> Puesto: {puesto.nombre_puesto} ({id_puesto})")
            empleados_puesto = [
                emp for emp in self.diccionario_empleados.values() if emp.id_puesto == id_puesto
            ]
            if empleados_puesto:
                for emp in empleados_puesto:
                    print(
                        f"   - ID: {emp.id_empleado} | Nombre: {emp.nombre} | Tel: {emp.telefono} | Correo: {emp.correo}")
            else:
                print("   (No hay empleados en este puesto)")

    def buscar_empleado_por_ID(self, busco_id_empleado):
        lista_empleados = list(self.diccionario_empleados.values())
        for i in range(len(lista_empleados)):
            if lista_empleados[i].id_empleado == busco_id_empleado:
                return  lista_empleados[i]
        return  None

    def eliminar_empleados_por_ID(self, buscar_id_empleado):
        lista_empleados = list(self.diccionario_empleados.values())
        for i in range(len(lista_empleados)):
            if lista_empleados[i].id_empleado == buscar_id_empleado:
                print(f"Esta seguro que quiere eliminar al empleado {buscar_id_empleado}")
                confirmacion = self.pedir_entero("Precione 1 para confirmar: "
                                                 "\nPrecine 2 para cancelar: ")
                if confirmacion == 1:
                    del self.diccionario_empleados[buscar_id_empleado]
                    print("Empeado eliminado con éxito... ")
                elif confirmacion == 2:
                    print("El empleado no se elimino... ")
                else:
                    print("Opción no valida... ")
            else:
                print(f"No se encontro ningun empleado con el ID {buscar_id_empleado} ")


gestion_empleados = GestionEmpleados()

class MenuGestionEmpleados:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO valido... ")


    def mostrar_menu_empleados(self):
        opcion = 0
        while opcion != 6:
            print("+++ MENU GESTION DE EMPLEADOS +++")
            print("1. Agregar Puesto de trabajo")
            print("2. Agregar empleado ")
            print("3. Mostrar lista de empleados por puesto ")
            print("4. Buscar emplado por ID de empleado")
            print("5. Elimimar empleados")
            print("6. Salir del menú gestio de empleados ")
            opcion = self.pedir_entero("Ingerse su opción: ")
            match opcion:
                case 1:
                    print("--- AGREGAR PUESTOS DE TRABAJO ---")
                    id_puesto = input("Ingrese el ID del puesto: ")
                    nombre_puesto = input("Ingrese el nombre del puesto: ")
                    gestion_empleados.agregar_puesto_empleado(id_puesto, nombre_puesto)

                case 2:
                    print("--- AGREGAR EMPLEADO ---")
                    cantidad = self.pedir_entero("Ingrese la cantidad de empleados que desea registrar: ")
                    for i in range(cantidad):
                        print(f"---Ingrese el empleado #{i+1} ---")
                        id_empleado = input("Ingrese el ID del empleado: ")
                        if id_empleado in gestion_empleados.diccionario_empleados:
                            print("Este ID ya existe, inntente de nuevo... ")
                            continue
                        nombre_empleado = input("Ingrese el nombre del empleado: ")
                        id_puesto = input("Ingrese el ID del puesto: ")
                        direccion_empleado = input("Ingrese la direccion del empleado: ")
                        tel_empleado = input("Ingrese el número de teléfono del empleado: ")
                        correo_empleado = input("Ingrese el correo del empleado: ")
                        gestion_empleados.agregar_empleado(id_empleado, nombre_empleado, id_puesto, direccion_empleado, tel_empleado, correo_empleado)
                        print("Empleado ingresado con éxito... ")

                case 3:
                    gestion_empleados.mostrar_empleados_por_puesto()
                case 4:
                    buscar_id = input("Ingrese el ID del enpleado a bucar: ")
                    empleado = gestion_empleados.buscar_empleado_por_ID(buscar_id)
                    if empleado:
                        puesto = gestion_empleados.diccionario_puestos_empleados.get(empleado.id_puesto)
                        nombre_puesto = puesto.nombre_puesto if puesto else "Sin puesto asignado"
                        print("\n=== Empleado encontrado ===")
                        print(f"ID: {empleado.id_empleado}")
                        print(f"Nombre: {empleado.nombre}")
                        print(f"Puesto: {nombre_puesto}")
                        print(f"Dirección: {empleado.direccion}")
                        print(f"Teléfono: {empleado.telefono}")
                        print(f"Correo: {empleado.correo}")
                    else:
                        print("Empleado no encontrado...")
                case 5:
                    eliminar_id = input("Ingrese el ID del empleado que desea eliminar: ")
                    gestion_empleados.eliminar_empleados_por_ID(eliminar_id)


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
            print("7. Salir del menú gestion de productos ")
            opcion = self.pedir_entero("Ingrese su opción: ")
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
                case 6:
                    print("------ELIMINAR PRODUCTOS----")
                    eliminar_producto = input("Ingrese el ID del producto a eliminar: ")
                    gestion.eliminar_producto(eliminar_producto)
                case 7:
                    print("Saliedo del menu de Gestión... ")
                case _:
                    print("Opción inválida, por favor intente nuevamente.")


menu_productos = MenuGestionProductos()
menu_gestion_clientes = MenuGestionDeClientes()
menu_gestion_empleados = MenuGestionEmpleados()
menu_principal = MenuPrincipal()


menu_principal.mostrar_menu_principal()
