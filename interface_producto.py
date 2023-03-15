import time
from prettytable import PrettyTable
from Producto import Producto
from conexionMongoDB import ConexionMongoDB
import os

class InterfaceProducto:
        def __init__(self):
            self.productos = Producto()
            self.conexion = ConexionMongoDB()

        def mostrarAcciones(self):
            opcion = 0
            existeConexion = self.conexion.conectarBD()
            if existeConexion:
                print(existeConexion)
            else:
                existeConexion = False
            self.productos.toDict()
            while opcion != 5:
                print("**Menu de Productos**")
                print("Seleccione una opcion: ")
                print("1. Agregar Producto")
                print("2. Mostrar Productos")
                print("3. Buscar Producto")
                print("4. Eliminar Producto")
                print("5. Salir")
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    self.agregarProducto()
                elif opcion == 2:
                    self.mostrarProductos()
                elif opcion == 3:
                    self.buscarProducto()
                elif opcion == 4:
                    self.eliminarProducto()
                elif opcion == 5:
                    print("Saliendo...") 

        def agregarProducto(self):
            existeConexion = self.conexion.conectarBD()
            print(existeConexion)
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripcion del producto: ")
            precio = input("Ingrese el precio del producto: ")
            producto = Producto(codigo, nombre, descripcion, precio)  
            pNuevo = producto.getDict()
            print("Agregando producto...")
            time.sleep(1)
            
            
            print("Producto agregado")
            print("Insertando en MongoDB...")
            self.conexion.insertar("Productos", pNuevo)
            print("Insertado en MongoDB exitosamente")
            
            self.productos.crear(pNuevo)
            time.sleep(1)
            print("Producto agregado")
            os.system ("cls")

        def mostrarProductos(self):
            tabla = PrettyTable()
            tabla.field_names = ["CODIGO", "NOMBRE", "DESCRIPCION DEL PRODUCTO", "PRECIO"]
            for producto in self.productos.mostrar():
                tabla.add_row([producto["codigo"], producto["nombre"], producto["descripcion"], producto["precio"]])
            print("Mostrando productos espera un segundo...")
            time.sleep(1)
            print(tabla)
            
        def buscarProducto(self):
            codigo = input("Ingrese el indice en el que se encuentra el producto: ")
            productos = self.productos.buscar(codigo)
            tabla = PrettyTable()
            tabla.field_names = ["CODIGO", "NOMBRE", "DESCRIPCION DEL PRODUCTO", "PRECIO"]
            if productos != None:
                tabla.add_row([productos["codigo"], productos["nombre"], productos["descripcion"], productos["precio"]])
                print("Buscando el producto espera un segundo...")
                time.sleep(1)
                print(tabla)
            else:
                print("El producto no existe")

        def eliminarProducto(self):
            eliminar = int(input("Ingrese el indice en el que se encuentra el producto: "))
            print("Eliminando...")
            time.sleep(1)
            self.productos.eliminar(eliminar)
            print("Producto eliminado")       

if __name__ == "__main__":
    interface = InterfaceProducto()
    interface.mostrarAcciones()