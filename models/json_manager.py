import json , os 

class Json_manager():
    def __init__(self, path):
        self.path = path

    def create_json(self) -> None:
        """
        Crea un archivo json vacio
        """
        with open(self.path, 'w') as f:
            json.dump([], f)

    def read_json(self)-> list:
        """
        Lee un archivo json y retorna su contenido
        en caso no exista el archivo retorna una lista vacia
        """
        if not os.path.exists(self.path):
            self.create_json()

        with open(self.path, 'r') as f:
            return json.load(f)
        

    def write_json(self, data: list) -> None:
        """
        Escribe en un archivo json el contenido de data
        """
        with open(self.path, 'w') as f:
            json.dump(data, f)


    def delete_json(self) -> None:
        """
        Elimina un archivo json
        """
        if os.path.exists(self.path):
            os.remove(self.path)
        else:
            print("The file does not exist")