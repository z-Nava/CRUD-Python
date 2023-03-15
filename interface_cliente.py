from prettytable import PrettyTable
from Cliente import Cliente
import conexionMongoDB as MongoDB
import time
import os
from alive_progress import alive_bar

class InterfaceCliente:
    
    def __init__(self):
        self.clientes = Cliente()
        self.testConexion = False

    def mostrarAcciones(self):
        try:
            testConexion = MongoDB.ConexionMongoDB().testConexion()
            if testConexion == True:
                self.testConexion = True

        except:
            print("Error de conexión")
            self.testConexion = False

        opcion = 0
        self.clientes.toDict()
        while opcion != 5:
            print("**Menu de Clientes**")
            print("Seleccione una opcion: ")
            print("1. Agregar Cliente")
            print("2. Mostrar Clientes")
            print("3. Buscar Cliente")
            print("4. Eliminar Cliente")
            print("5. Salir")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                self.agregarCliente()
            elif opcion == 2:
                self.mostrarClientes()
            elif opcion == 3:
                self.buscarCliente()
            elif opcion == 4:
                self.eliminarCliente()
            elif opcion == 5:
                print("Saliendo...")
            print("op1",opcion)
    
    def agregarCliente(self):
        rfc = input("Ingrese el RFC del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        cliente = Cliente(rfc, nombre, telefono)
        cNuevo = cliente.getDict()
        print("Agregando cliente...")
        time.sleep(1)
        
        print("Cliente agregado")
        print("Insertando en MongoDB...")
        mongo = MongoDB.ConexionMongoDB()
        mongo.insertar(cliente.getDict())
        print("Insertado en MongoDB exitosamente")
        mongo.cerrarConexion()

        time.sleep(1)
        self.clientes.crear(cNuevo)
        print("Cliente agregado")
        os.system ("cls")

    def mostrarClientes(self):
        tabla = PrettyTable()
        tabla.field_names = ["RFC", "NOMBRE", "TELEFONO"]
        for cliente in self.clientes.mostrar():
            tabla.add_row([cliente["rfc"], cliente["nombre"], cliente["telefono"]])
            os.system ("cls")
        print("Mostrando clientes...")
        time.sleep(1)
        print(tabla)
        
    def buscarCliente(self):
        rfc = input("Ingrese el indice en el que se encuentra el cliente: ")
        cliente = self.clientes.buscar(rfc)
        tabla = PrettyTable()
        tabla.field_names = ["RFC", "NOMBRE", "TELEFONO"]
        if cliente != None:
            tabla.add_row([cliente["rfc"], cliente["nombre"], cliente["telefono"]])
            os.system ("cls")
            print("Buscando cliente...")
            time.sleep(1)
            print("Cliente encontrado...")
            time.sleep(1)
            print(tabla)
        else:
            print("El cliente no existe")
            os.system ("cls")
       
    def eliminarCliente(self):
        eliminar = int(input("Escribe el indice del que eliminaras: "))
        print("Buscando cliente...")
        time.sleep(1)
        print("Eliminando cliente...")
        self.clientes.eliminar(eliminar)
        time.sleep(1)
        os.system ("cls")
        time.sleep(1)

    def comparacionDatos(self):
        datosJson = self.clientes.readDatos()
        datosDB = MongoDB.ConexionMongoDB()

        #actualizar datos

if __name__ == "__main__":
    interfaz = InterfaceCliente()
    interfaz.mostrarAcciones()

    

