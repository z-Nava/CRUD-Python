from Cliente import Cliente
from Producto import Producto
from Venta import Venta
import time
import os
import conexionMongoDB as MongoDB
#from menu_principal import MenuPrincipal
import time

from prettytable import PrettyTable

class InterfaceVenta:

    def __init__(self):
        self.ventas = Venta()
        self.clientes = Cliente()
        self.productos = Producto()
        self.listRespaldo = []
        
    def mostrarAcciones(self):
        self.clientes.toDict()
        self.productos.toDict()
        self.ventas.toDict()

        opcion = 0
        self.ventas.toDict()
        while opcion != 5:
            print("**Menu de Ventas**")
            print("Seleccione una opcion: ")
            print("1. Agregar Venta")
            print("2. Mostrar Ventas")
            print("3. Buscar Venta")
            print("4. Eliminar Venta")
            print("5. Salir")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                self.agregarVenta()
            elif opcion == 2:
                self.mostrarVentas()
            elif opcion == 3:
                self.buscarVenta()
            elif opcion == 4:
                self.eliminarVenta()
            elif opcion == 5:
                print("Saliendo al menu principal...")
                time.sleep(1)
                #MenuPrincipal.mostrarMenu(self.menuprin)
                
            
    def aggProducto(self, producto):
        self.listRespaldo.append(producto)

    def agregarVenta(self):
        self.ventas.LimplistVenta()
        cliente = input("Ingrese el indice en el que se encuentra el cliente: ")
        cliente = self.clientes.buscar(int(cliente))
        print(cliente)
        if cliente:
            print("--Agregar Productos--")
            saMenu = 0
            while saMenu != 2:
                detalle = input("Ingrese el indice del producto: ")
                self.ventas.crearListVenta(self.productos.buscar(int(detalle)))
                saMenu = int(input("Desea agregar otro producto? 1. Si 2. No: "))
            
            feVenta = input("Ingrese la fecha: ")
            toVenta = (int(input("Ingrese el total: ")))
            productos = self.ventas.regresarListaVenta()
            venta = Venta(cliente, productos, feVenta, toVenta)
            venDict = venta.getDict()

            print("Insertando en MongoDB...")
            mongo = MongoDB.ConexionMongoDB3()
            mongo.insertar(venta.getDict())
            print("Insertado en MongoDB exitosamente")
            mongo.cerrarConexion()

            self.ventas.crear(venDict)
            print("Venta agregada espera un segundo...")
            time.sleep(1)
            
    def mostrarVentas(self):
        tabla = PrettyTable()
        tabla.field_names = ["CLIENTE", "PRODUCTO", "FECHA", "TOTAL"]
        for venta in self.ventas.mostrar():
            nomCliente = venta["cliente"]["nombre"]
            tabla.add_row([nomCliente, " ", venta["fecha"], venta["total"]])
            for producto in venta["producto"]:
                nomProducto = producto["nombre"]
                tabla.add_row([" ", nomProducto, " ", " "])
        print(tabla)
        
    def buscarVenta(self):
        codigo = input("Ingrese el indice en el que se encuentra la venta: ")
        ventas = self.ventas.buscar(codigo)
        tabla = PrettyTable()
        tabla.field_names = ["CLIENTE", "PRODUCTO", "FECHA", "TOTAL"]
        if ventas != None:
            tabla.add_row([ventas["cliente"], ventas["producto"], ventas["fecha"], ventas["total"]])
            print("Buscando...")
            time.sleep(1)
            print(tabla)

    def eliminarVenta(self):
        codigo =  int(input("escribe el indice del que eliminaras:"))
        print("Eliminando...")
        time.sleep(1)
        self.ventas.eliminar(codigo)
        print("Venta eliminada permanentemente")
    

if __name__ == "__main__":
    interface = InterfaceVenta()
    interface.mostrarAcciones()

