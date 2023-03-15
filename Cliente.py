from Lista import Lista
import json
import os


class Cliente(Lista):

    def __init__(self, rfc="", nombre="", telefono="", file="cliente.json"):
        super().__init__("cliente.json")
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        self.file = file 

    def convertir(self):
        with open(self.file, 'r') as files:
            data = json.load(files)
            clientes = []
            for item in data:
                client = Cliente(item["rfc"], item["nombre"], item["telefono"])
                clientes.append(client)
        return clientes

    def getDict(self):
        if len(self.listas) > 0:
            array = []
            for i in self.listas:
                array.append(i.getDict())
            return array
        else:
            return {'rfc': self.rfc, 'nombre': self.nombre, 'telefono': self.telefono}

    def toDict(self):
        if os.path.exists("cliente.json"):
            diccionario = self.serializadorjson.readJson()
            for items in diccionario:
                cliente = Cliente(items["rfc"], items["nombre"], items["telefono"])
                dictclient = cliente.getDict()
                self.crear(dictclient)

    def readDatos(self, nombreLista = "Lista_Clientes"):
        lista = self.leerDocumento(nombreLista)
        return lista

if __name__ == "__main__":
    
    clientes = Cliente()
    clientes1 = Cliente("10", "Jose", "8713457555")
    clientes2 = Cliente("20", "Gael", "8713457555")
    clientes3 = Cliente("30", "Carlos", "8713457555")
    clientes.crear(clientes1)
    clientes.crear(clientes2)
    clientes.crear(clientes3)
    clBuscar = clientes.buscar("0")
    print(clBuscar)
    listado = clientes.mostrar()


    for cliente in listado:
        print("---------------------------")
        print(f"{cliente.rfc} |{cliente.nombre}|{cliente.telefono} |")
        print("---------------------------")

    #print("JSON ENCODER PERSONALIZADO")
    ##clienteJsonData = json.dumps(clientes1, indent=4 ,cls=ClienteEncoder)
    #clienteJsonData = open("clientes.json", "w")
    #print(clienteJsonData)

    



    


    
