from Lista import Lista
import json
from Cliente import Cliente
from serializadorJson import serializadorJson
import os
from Producto import Producto


class Venta(Lista):

    def __init__(self, cliente="", producto="", fecha="", total=0, file="Ventas.json"):
        super().__init__("Ventas.json")
        self.cliente = cliente
        self.producto = producto
        self.fecha = fecha
        self.total = total
        self.file = file

    def __str__(self):
        return f"Cliente: {self.cliente}\nProducto: {self.producto}\nFecha: {self.fecha}\nTotal: {self.total}\n"

    def getDict(self):
        if len(self.listas) > 0:
            array = []
            for i in self.listas:
                array.append(i.getDict())
            return array
        else:
            return {'cliente': self.cliente, 'producto': self.producto, 'fecha': self.fecha, 'total': self.total}

    def toDict(self):
        if os.path.exists("Ventas.json"):
            diccionario = self.serializadorjson.readJson()
            for items in diccionario:
                venta = Venta(items["cliente"], items["producto"], items["fecha"], items["total"])
                dictventa = venta.getDict()
                self.crear(dictventa)


if __name__ == "__main__":
    cliente = Cliente()
    producto = Producto()
    venta = Venta()
    producto1 = Producto("10", "Coca Cola", "Bebida", "1.5")
    producto2 = Producto("11", "Pepsi", "Bebida", "1.5")
    veDic = producto1.getDict()
    producto = producto.crear(veDic)
    veDic2 = producto2.getDict()
    producto = producto.crear(veDic2)

    producto.crearListVenta(producto1)
    producto.crearListVenta(producto2)

    cliente1 = Cliente("1", "Juan", "1234567890")
    clientedic = cliente1.getDict()
    cliente = cliente.crear(clientedic)
    print(cliente.mostrar())
    print(cliente.buscar(0))
    cliente = cliente.buscar(0)

    venta1 = Venta(cliente, producto, "2022", 30)
    ventadict = venta1.getDict()
    venta = venta.crear(ventadict)

    print(venta.mostrar())




