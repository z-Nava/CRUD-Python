import json
import os
from os.path import exists

class serializadorJson:
    def __init__(self, filename):
        self.filename = filename

    def writeJson(self, data):
        with open(self.filename, 'w') as archivo:
            json.dump(data, archivo, indent=4)

    def readJson(self):
        data=[]
        file_exists = exists(self.filename)
        if file_exists:
            with open(self.filename, 'r') as archivo:
                data = json.load(archivo)
        return data

