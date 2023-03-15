from serializadorJson import serializadorJson
class Lista:

    def __init__(self, file):
        super().__init__()
        self.serializadorjson = serializadorJson(file)
        self.listas_venta = []
        self.listas = []

    def crear(self, item):
        self.listas.append(item)
        self.serializadorjson.writeJson(self.listas)

    def mostrar(self):
        return self.listas

    def actualizar(self, index, item):
        self.listas[index] = item
        self.serializadorjson.writeJson(self.listas)

    def eliminar(self, index):
        del self.listas[index]
        self.serializadorjson.writeJson(self.listas)

    def buscar(self, cli):
        return self.listas[int(cli)]

    def LimplistVenta(self):
        self.listas_venta = []

    def crearListVenta(self, item):
        self.listas_venta.append(item)

    def regresarListaVenta(self):
        return self.listas_venta