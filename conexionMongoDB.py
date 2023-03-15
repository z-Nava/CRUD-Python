from pymongo import MongoClient
import pymongo
# Conexión a la base de datos MongoDB
class ConexionMongoDB:
    def __init__(self):
        self.db = ""
        self.cluster = "mongodb+srv://admin:televicion05@cluster0.uujrdgs.mongodb.net/?retryWrites=true&w=majority"

    def conectarBD(self):
        try:
            client = MongoClient(self.cluster)
            client.server_info()
            print("Conexión exitosa")
            self.db = client['CRUDpython']
            return True
        except Exception:
            print("No hay conexion a la base de datos, revisa tu conexion a internet!")
            return False

    def insertar(self, collection_nombre, datos):
        collection = self.db[collection_nombre]
        collection.insert_one(datos)
        
    def buscar(self, datos):
        return self.collection.find(datos)

    def eliminar(self, datos):
        self.collection.delete_one(datos)

    def actualizar(self, datos, datosNuevos):
        self.collection.update_one(datos, datosNuevos)

    def mostrar(self):
        for dato in self.collection.find():
            print(dato)

    def eliminarColeccion(self):
        self.collection.drop('Productos')

    def eliminarBaseDatos(self):
        self.client.drop_database()

    def cerrarConexion(self):
        self.client.close()

