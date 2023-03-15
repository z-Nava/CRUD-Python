from interface_cliente import InterfaceCliente
from interface_producto import InterfaceProducto
from interface_venta import InterfaceVenta
import os

class MenuPrincipal:

    def mostrarMenu(self):
        cliente = InterfaceCliente()
        producto = InterfaceProducto()
        venta = InterfaceVenta()
        opcion_g = 0
        while opcion_g != 4:
            print("**Menu Principal**")
            print("Seleccione una opcion_g: ")
            print("1. Clientes")
            print("2. Productos")
            print("3. Ventas")
            print("4. Salir")
            opcion_g = int(input("Seleccione una opcion_g: "))
            os.system ("cls")
            if opcion_g == 1:
                cliente.mostrarAcciones()
            elif opcion_g == 2:
                producto.mostrarAcciones()
            elif opcion_g == 3:
                venta.mostrarAcciones()
            elif opcion_g == 4:
                print("Saliendo...")
            print("op2",opcion_g)
            
    
if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrarMenu()
    