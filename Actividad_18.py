print("Actividad 18")
from  datetime import  datetime
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
        self.diccionario_categorias = {}
        self.diccionario_productos = {}
        self.cargar_categorias()
        self.cargar_productos()

    def cargar_categorias(self):
        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    id_categoria, nombre_categoria = linea.split(":")
                    self.diccionario_categorias[id_categoria] = Categoria(id_categoria, nombre_categoria)
        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creara uno al guardar... ")

    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for c in self.diccionario_categorias.values():
                archivo.write(f"{c.IDcategoria}:{c.nombre_categoria}\n")

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) != 5:
                        print(f"[productos.txt] Línea {num_linea} inválida (se esperan 5 campos): {linea}")
                        continue
                    id_producto, nombre, precio, id_categoria, stock = partes
                    try:
                        precio_f = float(precio)
                        stock_i = int(stock)
                    except ValueError:
                        print(f"[productos.txt] Línea {num_linea} valores numéricos inválidos: {linea}")
                        continue
                    self.diccionario_productos[id_producto] = Producto(id_producto, nombre, precio_f, id_categoria, stock=stock_i)
            print("Productos cargados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará al guardar")

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for p in self.diccionario_productos.values():
                archivo.write(f"{p.IDproducto}:{p.nombre_producto}:{p.precio}:{p.IDcategoria}:{p.stock}\n")

    def agregar_categoria(self, IDcategoria, nombre_categoria):
        self.diccionario_categorias[IDcategoria] = Categoria(IDcategoria, nombre_categoria)
        print("Categoria agregada con éxito")

    def agregar_producto(self, id_producto, nombre_producto, precio, id_categoria, stock):
        self.diccionario_productos[id_producto] = Producto(id_producto, nombre_producto, precio, id_categoria, stock=stock)
        self.guardar_productos()   # guardamos aquí para asegurar persistencia
        print("Producto ingresado con éxito... ")

    def buscar_producto_por_IDproducto(self, IDbuscado):
        lista = list(self.diccionario_productos.values())
        for i in range(len(lista)):
            if lista[i].IDproducto == IDbuscado:
                return lista[i]
        return None

    def eliminar_producto(self, IDbuscado):
        if IDbuscado in self.diccionario_productos:
            print(f"¿Seguro que quiere eliminar el producto {IDbuscado}?")
            while True:
                try:
                    confirmacion = int(input("Presione 1 para confirmar la eliminación\nPresione 2 para cancelar: "))
                except ValueError:
                    print("Error: ingrese un número válido.")
                    continue
                if confirmacion == 1:
                    del self.diccionario_productos[IDbuscado]
                    self.guardar_productos()
                    print(f"Producto con la ID: {IDbuscado} se ha eliminado con éxito.")
                    break
                elif confirmacion == 2:
                    print("El producto no se eliminó. ;)")
                    break
                else:
                    print("Opción inválida. Intente nuevamente...")
        else:
            print(f"No se encontró ningún producto con ID {IDbuscado}.")

    def modificar_producto(self, id_modificar, nuevo_precio=None, nuevo_stock=None):
        lista_productos = list(self.diccionario_productos.values())
        for i in range(len(lista_productos)):
            if lista_productos[i].IDproducto == id_modificar:
                if nuevo_precio is not None:
                    lista_productos[i].precio = nuevo_precio
                if nuevo_stock is not None:
                    lista_productos[i].stock = nuevo_stock
                self.diccionario_productos[id_modificar] = lista_productos[i]
                self.guardar_productos()
                print(f"Producto con ID {id_modificar} modificado con éxito.")
                return lista_productos[i]
        print(f"No se encontró un producto con ID {id_modificar}.")
        return None


gestion_productos = GestionProductos()

class Proveedores:
    def __init__(self, nit_empresa, nombre_empresa, direccion_empresa, telefono_empresa, correo_empresa):
        self.nit_empresa = nit_empresa
        self.nombre_empresa = nombre_empresa
        self.direccion_empresa = direccion_empresa
        self.telefono_empresa = telefono_empresa
        self.correo_empresa = correo_empresa

class GestionProveedores:
    def __init__(self):
        self.diccionario_proveedores = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea.strip(":"):
                        continue
                    nit_empresa, nombre_empresa, direccion_emrpresa, telefono_empresa, correo_emrpesa = linea.split(":")
                    self.diccionario_proveedores[nit_empresa] = Proveedores(nit_empresa, nombre_empresa, direccion_emrpresa, telefono_empresa, correo_emrpesa)
        except FileNotFoundError:
            print("No existe el archivo proveedodres.txt, se creará a guardar")

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for proveedores in self.diccionario_proveedores.values():
                archivo.write(f"{proveedores.nit_empresa}:{proveedores.nombre_empresa}:{proveedores.direccion_empresa}:{proveedores.telefono_empresa}:{proveedores.correo_empresa}")

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO valido... ")

    def crar_proveedor(self, nit_empresa, nombre_empresa, direccion_empresa, telefono_emrpesa, correo_empresa):
        self.diccionario_proveedores[nit_empresa] = Proveedores(nit_empresa, nombre_empresa, direccion_empresa, telefono_emrpesa, correo_empresa)
        self.guardar_proveedores()
        print(f"El proveedor {nombre_empresa}, fue agregado y guardado correctamente... ")

    def buscar_proveedor(self, busco_nit_empresa):
        lista_proveedores= list(self.diccionario_proveedores.values())
        for proveedor in lista_proveedores:
            if proveedor.nit_empresa == busco_nit_empresa:
                return proveedor
        return  None

    def modificar_datos_proveedor(self, nit_proveedor):
        if nit_proveedor in self.diccionario_proveedores:
            proveedor = self.diccionario_proveedores[nit_proveedor]
            print(f"Cliente encontrado {proveedor.nombre_proveedor}")
            print("¿Que datos desea modificar?: ")
            print("1. Correo")
            print("2. Teléfono")
            opcion = self.pedir_entero("")
            if opcion == 1:
                nuevo_correo = input("Ingrese el nuevo correo del proveedor: ")
                proveedor.correo_emrpresa = nuevo_correo
            if opcion == 2:
                nuevo_telefono = input("Ingrese el nuevo teléfono del proveedor: ")
                proveedor.telfono_empresa = nuevo_telefono
            else:
                print("Opción invalida... ")
                return
            self.guardar_proveedores()
            print("Proveedor actualizado correctamente")
        else:
            print(f"El {nit_proveedor} no fue encontrado")

    def eliminar_proveedor(self, eliminar_nit_proveedor):
        if eliminar_nit_proveedor in self.diccionario_proveedores:
            eliminar_proveedor = self.diccionario_proveedores[eliminar_nit_proveedor]
            print(f"Seguro que quiere eliminar al proveedor {eliminar_proveedor.nombre_empresa} con el NIT {eliminar_nit_proveedor}? ")
            print("Precione 1 para confirmar: ")
            print("Precione 2 para cancelar: ")
            confirmacion = self.pedir_entero("Ingrese su opción: ")
            if confirmacion == 1:
                del self.diccionario_proveedores[eliminar_nit_proveedor]
                self.guardar_proveedores()
                print("Cliente eliminado con éxito... ")
            else:
                print("Eliminación cancelada... ")
        else:
            print(f"No se encontro al proveedor con el NIT: {eliminar_nit_proveedor}")

    def quicksort_proveedores(self, lista_proveedores):
        if len(lista_proveedores) <= 1:
            return lista_proveedores
        pivot = lista_proveedores[0]
        menores = [p for p in lista_proveedores[1:] if p.nombre_empresa.lower() <= pivot.nombre_empresa.lower()]
        mayores = [p for p in lista_proveedores[1:] if p.nombre_empresa.lower() > pivot.nombre_empresa.lower()]
        return self.quicksort_proveedores(menores) + [pivot] + self.quicksort_proveedores(mayores)

    def mostar_proveedores_ordenados(self):
        lista = list(self.diccionario_proveedores.values())
        ordenados = self.quicksort_proveedores(lista)
        print(f"Lista de proveedores ordenados por nombre: ")
        for p in ordenados:
            print(f"{p.nit_empresa} | {p.nombre_empresa} | {p.direccion_empresa} | {p.telefono_empresa} | {p.correo_empresa}")

gestion_proveedores = GestionProveedores()

class MenuGestionProveedores:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return  int(input(mensaje))
            except ValueError:
                print("Ingrse un  NUMERO valido")

    def mostrar_menu_gestion_proveedores(self):
        opcion = 0
        while opcion != 6:
            print("MENU GESTION PROVEEDORES")
            print("1. Agregar proveedores")
            print("2. Mostrar provedores")
            print("3. Modificar proveedor")
            print("4. Buscar proveedores")
            print("5. Eliminar proveedor")
            print("6. Salir del menú de proveedores")
            opcion = self.pedir_entero("Ingerese su opción: ")
            match opcion:
                case 1:
                    cantidad = self.pedir_entero("¿Cuantos proveedores desea ingrasar?: ")
                    for i in range(cantidad):
                        print(f"f\n Ingrese proveedor {i+1}: ")
                        while True:
                            nit_proveedor = input("Ingrese el nit del proveedor: ")
                            if nit_proveedor in gestion_proveedores.diccionario_proveedores:
                                print(f"El nit {nit_proveedor} ya existe en el sistema...")
                            else:
                                break
                        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
                        direccion_proveedor = input("Ingrese la direección del proveedor: ")
                        tel_proveedor = input("Ingrese el teléfono del proveedor: ")
                        correo_proveedor = input("Ingrese el correo del proveedor: ")
                        gestion_proveedores.crar_proveedor(nit_proveedor, nombre_proveedor, direccion_proveedor, tel_proveedor, correo_proveedor)
                        print("Proveedor agregado con éxito...")
                case 2:
                    gestion_proveedores.mostar_proveedores_ordenados()
                case 3:
                    print("+++MODIFICAR PROVEEDOR+++")
                    nit_proveedor_modifcar = input("Ingrese el Nit del proveedor: ")
                    gestion_proveedores.modificar_datos_proveedor(nit_proveedor_modifcar)
                case 4:
                    buco = input("Ingrese el Nit de la empresa que busca: ")
                    gestion_proveedores.buscar_proveedor(buco)
                case 5:
                    eliminar = input("Ingrese el Nit de la empresa que desaea aliminar: ")
                    gestion_proveedores.eliminar_proveedor(eliminar)
                case 6:
                    print("Saliendo del menú de proveedores")
                case _:
                    print("Opción inválida, por favor intente nuevamente.")


class Clientes:
    def __init__(self, nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente):
        self.nit_cliente = nit_cliente
        self.nombre_cliente = nombre_cliente
        self.direccion_cliente = direccion_cliente
        self.tel_cliente = tel_cliente
        self.correo_cliente = correo_cliente

class GestionClientes:
    def __init__(self):
        self.diccionario_clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) != 5:
                        print(f"[clientes.txt] Línea {num_linea} inválida (se esperan 5 campos): {linea}")
                        continue
                    nit_cliente, nombre_cliente, direccion, telefono, correo = partes
                    self.diccionario_clientes[nit_cliente] = Clientes(nit_cliente, nombre_cliente, direccion, telefono, correo)
            print("Clientes cargados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará al guardar")

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for cliente in self.diccionario_clientes.values():
                archivo.write(f"{cliente.nit_cliente}:{cliente.nombre_cliente}:{cliente.direccion_cliente}:{cliente.tel_cliente}:{cliente.correo_cliente}\n")

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO valido...")

    def crear_cliente(self, nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente):
        self.diccionario_clientes[nit_cliente] = Clientes(nit_cliente, nombre_cliente, direccion_cliente, tel_cliente, correo_cliente)
        self.guardar_clientes()
        print(f"Cliente {nombre_cliente} agregado y guardado correctamente ;)")

    def quicksort_clientes(self, clientes):
        if len(clientes) <= 1:
            return clientes
        pivot = clientes[0]
        menores = [c for c in clientes[1:] if c.nombre_cliente.lower() <= pivot.nombre_cliente.lower()]
        mayores = [c for c in clientes[1:] if c.nombre_cliente.lower() > pivot.nombre_cliente.lower()]
        return self.quicksort_clientes(menores) + [pivot] + self.quicksort_clientes(mayores)

    def buscar_cliente_por_nit(self, busco_nit_cliente):
        lista_clientes = list(self.diccionario_clientes.values())
        for j in range(len(lista_clientes)):
            if lista_clientes[j].nit_cliente == busco_nit_cliente:
                return lista_clientes[j]
        return None

    def modificar_datos_cliente(self, nit):
        if nit in self.diccionario_clientes:
            cliente = self.diccionario_clientes[nit]
            print(f"Cliente encontrado: {cliente.nombre_cliente}")
            print("¿Qué dato desea modificar?")
            print("1. Correo")
            print("2. Teléfono")
            opcion = self.pedir_entero("Ingrese la Opción que desea modificar: ")
            if opcion == 1:
                nuevo_correo = input("Ingrese el nuevo correo del cliente: ")
                cliente.correo_cliente = nuevo_correo
            elif opcion == 2:
                nuevo_telefono = input("Ingrese el nuevo Teléfono del cliente: ")
                cliente.tel_cliente = nuevo_telefono
            else:
                print("Opción inválida.")
                return
            self.guardar_clientes()
            print("Datos modificados y guardados con éxito.")
        else:
            print(f"No se encontró un cliente con el NIT: {nit}")

    def eliminar_clientes(self, nit_cliente):
        if nit_cliente in self.diccionario_clientes:
            cliente = self.diccionario_clientes[nit_cliente]
            print(f"¿Seguro que quiere eliminar al cliente {cliente.nombre_cliente} con el NIT: {cliente.nit_cliente}?")
            confirmacion = self.pedir_entero("Ingrese 1 para confirmar o 2 para cancelar: ")
            if confirmacion == 1:
                del self.diccionario_clientes[nit_cliente]
                self.guardar_clientes()
                print("Cliente eliminado con éxito... ")
            else:
                print("Eliminación cancelada")
        else:
            print(f"No se encontró un cliente con el NIT: {nit_cliente}")

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
                            print("Cliente creado con éxito ;)")
                            break
                case 2:
                    if not gestion_clientes.diccionario_clientes:
                        print("No hay clientes registrados...")
                    else:
                        print("----- LISTA DE CLIENTES ORDENADA -----")
                        lista_clientes = list(gestion_clientes.diccionario_clientes.values())
                        lista_ordenada = gestion_clientes.quicksort_clientes(lista_clientes)
                        for c in lista_ordenada:
                            print(f"NIT: {c.nit_cliente} | Nombre: {c.nombre_cliente} | Dirección: {c.direccion_cliente} | Tel: {c.tel_cliente} | Correo: {c.correo_cliente}")
                case 3:
                    if not gestion_clientes.diccionario_clientes:
                        print("No hay clientes registrados... ")
                    else:
                        print("-----BUSCAR CLIENTE POR NIT-----")
                        buscar_nit = input("Ingrese el nit del cliente: ")
                        encontrado = gestion_clientes.buscar_cliente_por_nit(buscar_nit)
                        if encontrado:
                            print(f"El cliente con el NIT {encontrado.nit_cliente} es {encontrado.nombre_cliente}")
                        else:
                            print("Cliente no encontrado...")
                case 4:
                    print("---MODIFICAR DATOS--- ")
                    nit_cliente_modificar = input("Ingrese el NIT del cliente para buscarlo: ")
                    gestion_clientes.modificar_datos_cliente(nit_cliente_modificar)
                case 5:
                    print("---ELIMINAR CLIENTES---")
                    eliminar = input("Ingrese el NIT del cliente que desea eliminar: ")
                    gestion_clientes.eliminar_clientes(eliminar)
                case 6:
                    print("Saliendo del menu de clientes...")
                case _:
                    print("Opción inválida, por favor intente nuevamente.")


class MenuPrincipal:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error ingrese un NUMERO valido...")

    def mostrar_menu_principal(self):
        opcion = 0
        while opcion != 6:
            print("+++Menu General+++")
            print("1. Gestion de productos")
            print("2. Gestion de clientes")
            print("3. Gestion de empleados")
            print("4. Gestion de proveedores")
            print("5. Gestion de ventas")
            print("6. Salir del programa")
            opcion = self.pedir_entero("Ingrese su opción: ")
            match opcion:
                case 1:
                    menu_productos.mostrar_menu_productos()
                case 2:
                    menu_gestion_clientes.mostrar_menu_gestion_clientes()
                case 3:
                    menu_gestion_empleados.mostrar_menu_empleados()
                case 4:
                    menu_gestion_proveedores.mostrar_menu_gestion_proveedores()
                case 5:
                    menu_gestion_ventas.mostrar_menu_gestion_ventas()
                case 6:
                    print("Saliendo del programa")
                case _:
                    print("Opción inválida, por favor intente nuevamente.")


class PuestosDeEmpleado:
    def __init__(self, id_puesto, nombre_puesto):
        self.id_puesto = id_puesto
        self.nombre_puesto = nombre_puesto

class Empleados:
    def __init__(self, id_empleado, nombre, id_puesto, direccion, telefono, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.id_puesto = id_puesto
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class GestionEmpleados:
    def __init__(self):
        self.diccionario_puestos_empleados = {}
        self.diccionario_empleados = {}
        self.cargar_empleados()

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) != 6:
                        print(f"[empleados.txt] Línea {num_linea} inválida (se esperan 6 campos): {linea}")
                        continue
                    id_empleado, nombre_empleado, id_puesto, direccion_empleado, telefono_empleado, correo_empleado = partes
                    self.diccionario_empleados[id_empleado] = Empleados(id_empleado, nombre_empleado, id_puesto, direccion_empleado, telefono_empleado, correo_empleado)
            print("Empleados cargados desde empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt se creará uno al guardar.")

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for e in self.diccionario_empleados.values():
                archivo.write(f"{e.id_empleado}:{e.nombre}:{e.id_puesto}:{e.direccion}:{e.telefono}:{e.correo}\n")

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO VALIDO...")

    def agregar_puesto_empleado(self, IDpuesto, nombre_puesto):
        self.diccionario_puestos_empleados[IDpuesto] = PuestosDeEmpleado(IDpuesto, nombre_puesto)
        print("Puesto de empleado agregado con éxito... ")

    def agregar_empleado(self, IDempledo, nombre_empleado, IDpuesto, direccion_empleado, telefono_empleado, correo_empleado):
        self.diccionario_empleados[IDempledo] = Empleados(IDempledo, nombre_empleado, IDpuesto, direccion_empleado, telefono_empleado, correo_empleado)
        self.guardar_empleados()
        print("Empleado agregado con éxito... ")

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
                    print(f"   - ID: {emp.id_empleado} | Nombre: {emp.nombre} | Tel: {emp.telefono} | Correo: {emp.correo}")
            else:
                print("   (No hay empleados en este puesto)")

    def buscar_empleado_por_ID(self, busco_id_empleado):
        lista_empleados = list(self.diccionario_empleados.values())
        for i in range(len(lista_empleados)):
            if lista_empleados[i].id_empleado == busco_id_empleado:
                return lista_empleados[i]
        return None

    def eliminar_empleados_por_ID(self, buscar_id_empleado):
        if buscar_id_empleado in self.diccionario_empleados:
            empleado = self.diccionario_empleados[buscar_id_empleado]
            print(f"¿Está seguro que quiere eliminar al empleado {empleado.nombre} (ID: {buscar_id_empleado})?")
            confirmacion = self.pedir_entero("Precione 1 para confirmar:\nPrecione 2 para cancelar: ")
            if confirmacion == 1:
                del self.diccionario_empleados[buscar_id_empleado]
                self.guardar_empleados()
                print("Empleado eliminado con éxito... ")
            else:
                print("El empleado no se eliminó...")
        else:
            print(f"No se encontró ningún empleado con el ID {buscar_id_empleado}")

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
            print("5. Eliminar empleados")
            print("6. Salir del menú gestion de empleados ")
            opcion = self.pedir_entero("Ingrese su opción: ")
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
                            print("Este ID ya existe, intente de nuevo... ")
                            continue
                        nombre_empleado = input("Ingrese el nombre del empleado: ")
                        id_puesto = input("Ingrese el ID del puesto: ")
                        direccion_empleado = input("Ingrese la direccion del empleado: ")
                        tel_empleado = input("Ingrese el número de teléfono del empleado: ")
                        correo_empleado = input("Ingrese el correo del empleado: ")
                        gestion_empleados.agregar_empleado(id_empleado, nombre_empleado, id_puesto, direccion_empleado, tel_empleado, correo_empleado)
                case 3:
                    gestion_empleados.mostrar_empleados_por_puesto()
                case 4:
                    buscar_id = input("Ingrese el ID del empleado a buscar: ")
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
        while opcion != 8:
            print("+++ MENU GESTION DE PRODUCTOS +++")
            print("1. Agregar categorias de productos")
            print("2. Agregar producto")
            print("3. Mostrar lista de categorias")
            print("4. Mostrar lista de productos")
            print("5. Buscar producto por codigo")
            print("6. Eliminar productos")
            print("7. Actualizar productos")
            print("8. Salir del menú gestion de productos ")
            opcion = self.pedir_entero("Ingrese su opción: ")
            match opcion:
                case 1:
                    id_categoria = input("Ingrese el ID de la categoria: ")
                    nombre_categoria = input("Ingrese el nombre de la categoria: ")
                    gestion_productos.agregar_categoria(id_categoria, nombre_categoria)
                    gestion_productos.guardar_categorias()
                case 2:
                    id_producto = input("Ingrese el ID del producto: ")
                    if id_producto in gestion_productos.diccionario_productos:
                        print("Este ID de producto ya existe.")
                        continue
                    nombre_producto = input("Ingrese el nombre del producto: ")
                    precio_producto = float(input("Ingrese el precio del producto: Q"))
                    id_cat = input("Ingrese el ID de la categoria: ")
                    if id_cat not in gestion_productos.diccionario_categorias:
                        print("ERROR, primero agregue la categoria del producto...")
                    else:
                        stock = int(input("Ingrese el stock inicial: "))
                        gestion_productos.agregar_producto(id_producto, nombre_producto, precio_producto, id_cat, stock=stock)
                case 3:
                    if not gestion_productos.diccionario_categorias:
                        print("No hay categorias registradas... ")
                    else:
                        print("-----LISTA DE CATEGORIAS-----")
                        cont = 1
                        for cat in gestion_productos.diccionario_categorias.values():
                            print(f"{cont}- ID de categoria: {cat.IDcategoria}, Nombre de categoria: {cat.nombre_categoria}")
                            cont += 1
                case 4:
                    if not gestion_productos.diccionario_productos:
                        print("No hay productos ingresados... ")
                    else:
                        print("-----LISTA DE PRODUCTOS POR CATEGORIA------")
                        for cat in gestion_productos.diccionario_categorias.values():
                            print(f"\n>> Categoría: {cat.nombre_categoria} ({cat.IDcategoria})")
                            encontrados = False
                            for p in gestion_productos.diccionario_productos.values():
                                if p.IDcategoria == cat.IDcategoria:
                                    print(f"   - [{p.IDproducto}] {p.nombre_producto} | Precio: Q{p.precio} | Stock: {p.stock}")
                                    encontrados = True
                            if not encontrados:
                                print("No hay productos en esta categoria... ")
                case 5:
                    print("------BUSCAR PRODUCTO POR CODIGO-----")
                    buscar_codigo = input("Ingrese el codigo que desea buscar: ")
                    encontrado = gestion_productos.buscar_producto_por_IDproducto(buscar_codigo)
                    if encontrado:
                        print(f"Producto encontrado: {encontrado.IDproducto} | Nombre: {encontrado.nombre_producto} | Precio: {encontrado.precio} | Stock: {encontrado.stock}")
                    else:
                        print("Producto no encontrado... ")
                case 6:
                    print("------ELIMINAR PRODUCTOS----")
                    eliminar_producto = input("Ingrese el ID del producto a eliminar: ")
                    gestion_productos.eliminar_producto(eliminar_producto)
                case 7:
                    modificar_id = input("Ingrese el ID del producto que desea modificar: ")
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    nuevo_stock = int(input("Ingrese el nuevo stock: "))
                    gestion_productos.modificar_producto(modificar_id, nuevo_precio, nuevo_stock)
                case 8:
                    print("Saliendo del menú de gestion de productos... ")
                case _:
                    print("Opción inválida, por favor intente nuevamente.")

class DetealleDeVentas:
    def __init__(self, id_detalle, id_venta, id_producto, cantidad, subtotal, stock_actual):
        self.id_detalle = id_detalle
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal
        self.stock_actual = stock_actual

class Ventas:
    def __init__(self, id_venta, id_empleado, nit_cliente, id_producto, contidad, total, fecha):
        self.id_venta = id_venta
        self.id_empleado = id_empleado
        self.nit_cliente = nit_cliente
        self.id_producto = id_producto
        self.contidad = contidad
        self.total = total
        self.fecha = fecha
        self.lista_detalles_de_venta = []

class GestionVentas:
    def __init__(self):
        self.diccionario_ventas = {}
        self.diccionario_detalles_ventas = {}
        self.cargar_ventas()
        self.cargar_detalles()

    def cargar_detalles(self):
        try:
            with open("detalles_ventas.txt", "r", encoding="utf-8") as archivo:
                for num_linea, linea in enumerate(archivo, start=1):
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(":")
                        if len(partes) != 6:
                            print(f"Línea {num_linea} inválida en detalles_ventas.txt: {linea}")
                            continue
                        id_detalle, id_venta, id_producto, cantidad, subtotal, stock_actual = partes
                        try:
                            self.diccionario_detalles_ventas[id_detalle] = DetealleDeVentas(
                                id_detalle=id_detalle,
                                id_venta=id_venta,
                                id_producto=id_producto,
                                cantidad=int(cantidad),
                                subtotal=float(subtotal),
                                stock_actual=int(stock_actual)
                            )
                        except ValueError:
                            print(f"Error de conversión en la línea {num_linea}: {linea}")
            print("Detalles de ventas importados desde detalles_ventas.txt")
        except FileNotFoundError:
            print("No existe el archivo detalles_ventas.txt, se creará uno al guardar.")

    def cargar_ventas(self):
        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_venta, id_empleado, nit_cliente, id_producto, cantidad, total, fecha = linea.split(":")
                        self.diccionario_ventas[id_venta] = {
                            "Empleado": id_empleado,
                            "Cliente": nit_cliente,
                            "Producto": id_producto,
                            "Cantidad": int(cantidad),
                            "Total": float(total),
                            "Fecha": fecha
                        }
            print("Ventas importadas desde ventas.txt")
        except FileNotFoundError:
            print("No existe el arhivo ventas.txt, se creara uno al guardar.")

    def guardar_detalles(self):
        with open("detalles_ventas.txt", "w", encoding="utf-8") as archivo:
            for id_detalle, detalle in self.diccionario_detalles_ventas.items():
                archivo.write(f"{detalle.id_detalle}:{detalle.id_venta}:{detalle.id_producto}:"
                              f"{detalle.cantidad}:{detalle.subtotal}:{detalle.stock_actual}\n")
        print("Detalles de ventas guardados en detalles_ventas.txt")

    def generar_id_detalle(self):
        if not self.diccionario_detalles_ventas:
            return "D1"
        else:
            ultimo_id = max(self.diccionario_detalles_ventas.keys())
            numero = int(ultimo_id[1:])
            nuevo_numero = numero + 1
            return f"D{nuevo_numero:04d}"

    def guardar_venta(self):
        with open("ventas.txt", "w", encoding="utf-8") as archivo:
            for id_venta, datos in self.diccionario_ventas.items():
                archivo.write(f"{id_venta}:{datos['Empleado']}:{datos['Cliente']}:{datos['Producto']}:{datos['Cantidad']}:{datos['Total']}:{datos['Fecha']}\n")

    def generar_id_venta(self):
        if not  self.diccionario_ventas:
            return "V1"
        else:
            ultimo_id = max(self.diccionario_ventas.keys())
            numero = int(ultimo_id[1:])
            nuevo_numero = numero+1
            return f"V{nuevo_numero:04d}"

    def crear_venta(self, id_empleado, nit_cliente, id_producto, cantidad):
        if id_empleado not in gestion_empleados.diccionario_empleados:
            print(f"ERROR, el empleado no existe... ")
            return
        if nit_cliente not in gestion_clientes.diccionario_clientes:
            print(f"El cliente con el Nit {nit_cliente} no existe, se registrará ahora:")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            direccion_cliente = input("Ingrese la dirección del cliente: ")
            telefono_cliente = input("Ingrese el teléfono del cliente: ")
            correo_cliente = input("Ingrese el correo del cliente: ")
            gestion_clientes.diccionario_clientes[nit_cliente] = {
                "Nombre": nombre_cliente,
                "Direccion": direccion_cliente,
                "Telefono": telefono_cliente,
                "Correo": correo_cliente
            }
            gestion_clientes.guardar_clientes()
            print(f"Cliente {nombre_cliente} creado exitosamente ;)")
        if id_producto not in gestion_productos.diccionario_productos:
            print(f"ERROR, el producto {id_producto} no existe")
            return
        producto = gestion_productos.diccionario_productos[id_producto]
        if producto.stock < cantidad:
            print("ERROR, no hay suficiente stock")
            return
        total = cantidad * producto.precio
        id_venta = self.generar_id_venta()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.diccionario_ventas[id_venta] = {
            "Empleado": id_empleado,
            "Cliente": nit_cliente,
            "Producto": id_producto,
            "Cantidad": cantidad,
            "Total": total,
            "Fecha": fecha_actual
        }
        producto.stock -= cantidad
        gestion_productos.guardar_productos()
        self.guardar_venta()
        id_detalle = self.generar_id_detalle()
        detalle = DetealleDeVentas(
            id_detalle=id_detalle,
            id_venta=id_venta,
            id_producto=id_producto,
            cantidad=cantidad,
            subtotal=total,
            stock_actual=producto.stock
        )
        self.diccionario_detalles_ventas[id_detalle] = detalle
        self.guardar_detalles()
        print(f"Venta {id_venta} registrada con éxito en {fecha_actual}. Total: Q{total}")
        print(f"Detalle de venta {id_detalle} creado correctamente.")

    def mostrar_todas_las_ventas(self):
        if not  self.diccionario_ventas:
            print("No hay ventas registradas")
        else:
            print("\n===LISTA DE TODAS LAS VENTAS===")
            for id_venta, datos in self.diccionario_ventas.items():
                print(f"\nVenta: {id_venta}")
                print(f"  Empleado: {datos['Empleado']}")
                print(f"  Cliente (NIT): {datos['Cliente']}")
                print(f"  Producto: {datos['Producto']}")
                print(f"  Cantidad: {datos['Cantidad']}")
                print(f"  Total: Q{datos['Total']}")
                print(f"  Fecha: {datos['Fecha']}")

    def mostrar_ventas_por_categoria(self, categoria):
        ventas_encontradas = False
        print(f"\n=== VENTAS DE LA CATEGORÍA: {categoria} ===")
        for id_venta, datos in self.diccionario_ventas.items():
            id_producto = datos["Producto"]
            if id_producto in gestion_productos.diccionario_productos:
                producto = gestion_productos.diccionario_productos[id_producto]
                if producto.categoria.lower() == categoria.lower():
                    ventas_encontradas = True
                    print(f"\nVenta: {id_venta}")
                    print(f"  Empleado: {datos['Empleado']}")
                    print(f"  Cliente (NIT): {datos['Cliente']}")
                    print(f"  Producto: {producto.nombre} ({producto.id_producto})")
                    print(f"  Cantidad: {datos['Cantidad']}")
                    print(f"  Total: Q{datos['Total']}")
                    print(f"  Fecha: {datos['Fecha']}")
        if not ventas_encontradas:
            print(f"No se encontraron ventas en la categoría '{categoria}'.")

    def mostrar_ventas_del_dia(self):
        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        ventas_encontradas = False
        print(f"\n=== VENTAS DEL DÍA {fecha_hoy} ===")
        for id_venta, datos in self.diccionario_ventas.items():
            # la fecha en ventas es "YYYY-MM-DD HH:MM:SS"
            if datos["Fecha"].startswith(fecha_hoy):
                ventas_encontradas = True
                print(f"\nVenta: {id_venta}")
                print(f"  Empleado: {datos['Empleado']}")
                print(f"  Cliente (NIT): {datos['Cliente']}")
                print(f"  Producto: {datos['Producto']}")
                print(f"  Cantidad: {datos['Cantidad']}")
                print(f"  Total: Q{datos['Total']}")
                print(f"  Fecha: {datos['Fecha']}")
        if not ventas_encontradas:
            print("Hoy no se han realizado ventas.")

    def buscar_ventas(self, criterio):
        print(f"\n=== RESULTADOS DE LA BÚSQUEDA: {criterio} ===")
        ventas_encontradas = False
        for id_venta, datos in self.diccionario_ventas.items():
            if (criterio.lower() in id_venta.lower() or
                    criterio.lower() in datos["Cliente"].lower() or
                    criterio.lower() in datos["Producto"].lower()):
                ventas_encontradas = True
                print(f"\nVenta: {id_venta}")
                print(f"  Empleado: {datos['Empleado']}")
                print(f"  Cliente (NIT): {datos['Cliente']}")
                print(f"  Producto: {datos['Producto']}")
                print(f"  Cantidad: {datos['Cantidad']}")
                print(f"  Total: Q{datos['Total']}")
                print(f"  Fecha: {datos['Fecha']}")
            if not ventas_encontradas:
                print("No se encontraron ventas con ese criterio.")

gestion_ventas = GestionVentas()

class MenuGestionVentas:
    def pedir_entero(self, mensaje):
        while True:
            try:
                return  int(input(mensaje))
            except ValueError:
                print("Ingrese un NUMERO valido")

    def mostrar_menu_gestion_ventas(self):
        opcion = 0
        while opcion != 6:
            print("\n===MENU DE GESTION DE VENTAS===")
            print("1. Realizar una venta")
            print("2. Mostrar todas las ventas")
            print("3. Mostrar las ventas por categoria")
            print("4. Mostrar ventas realizadas en el dia")
            print("5. Buscar ventas realizadas")
            print("6. Salir del menú de gestion de ventas")
            opcion = self.pedir_entero("Ingrese su opción: ")
            match opcion:
                case 1:
                    id_empleado = input("Ingrese su ID: ")
                    nit_cliente = input("Ingrese el Nit del cliente: ")
                    id_producto = input("Ingrsae el ID del producto: ")
                    cantidad = self.pedir_entero("Ingrese la cantidad a vender: ")

                    gestion_ventas.crear_venta(id_empleado, nit_cliente, id_producto, cantidad)
                case 2:
                    gestion_ventas.mostrar_todas_las_ventas()
                case 3:
                    categoria = input("Ingrese la categoria que desea consultar: ")
                    gestion_ventas.mostrar_ventas_por_categoria(categoria)
                case 4:
                    gestion_ventas.mostrar_ventas_del_dia()
                case 5:
                    criterio = input("Ingrese el ID de venta, NIT del cliente o ID del producto a buscar: ")
                    gestion_ventas.buscar_ventas(criterio)
                case 6:
                    print("Saliedo del menú de gestion de ventas...")




menu_productos = MenuGestionProductos()
menu_gestion_clientes = MenuGestionDeClientes()
menu_gestion_empleados = MenuGestionEmpleados()
menu_gestion_proveedores = MenuGestionProveedores()
menu_gestion_ventas = MenuGestionVentas()
menu_principal = MenuPrincipal()

menu_principal.mostrar_menu_principal()
