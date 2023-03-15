from Lista import Lista
import json
from serializadorJson import serializadorJson
import os


class Producto(Lista):

    def __init__(self, codigo="", nombre="", descripcion="", precio=0, file="producto.json"):
        super().__init__("producto.json")
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.file = file

    def convertir(self):
        with open(self.file, 'r') as files:
            data = json.load(files)
            productos = []
            for item in data:
                product = Producto(item["codigo"], item["nombre"], item["descripcion"], item["precio"])
                productos.append(product)
        return productos

    def getDict(self):
        if len(self.listas) > 0:
            array = []
            for i in self.listas:
                array.append(i.getDict())
            return array
        else:
            return {'codigo': self.codigo, 'nombre': self.nombre, 'descripcion': self.descripcion,
                    'precio': self.precio}

    def toDict(self):
        if os.path.exists("producto.json"):
            diccionario = self.serializadorjson.readJson()
            for items in diccionario:
                product = Producto(items["codigo"], items["nombre"], items["descripcion"], items["precio"])
                dictproduct = product.getDict()
                self.crear(dictproduct)


if __name__ == "__main__":
    producto = Producto()
    producto1 = Producto("100", "Coca-Cola", "Bebida", "20.00")
    producto2 = Producto("200", "Ruffles", "Fritura", "15.00")
    producto3 = Producto("300", "Jugo durazno", "Bebida", "20.00")
    producto.crear(producto1)
    producto.crear(producto2)
    producto.crear(producto3)

    venta_nueva = Producto("400", "Emperador Chocolate", "Galletas", "31.00")
    producto.actualizar(2, venta_nueva)
    producto.eliminar(1)

    listado = producto.mostrar()
    data= serializadorJson("Productos.json")
    data.writeJson(Producto.serialize(1, listado))

    def writeJson(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, cls=serializadorJson)

    for producto in listado:
        print("---------------------------")
        print(f"{producto.codigo} |{producto.nombre}|{producto.descripcion} |{producto.precio}")

    

    
