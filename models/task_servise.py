from datetime import datetime

from .json_manager import Json_manager

path_json = 'tasks.json'

json_manager = Json_manager(path_json)

class Task():
    id : int 
    description : str
    status : str
    created_at : datetime
    updated_at : datetime
    
    def __init__(self, id : int, description : str, status : str, created_at : datetime, updated_at : datetime):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

class Task_service():
    def __init__(self):
        pass

    def list_tasks(self) -> dict:
        """
        Lista todas las tareas
        """
        data = json_manager.read_json()
        return data
    
    def get_tast(self, id:int) -> dict:
        """
        Obtiene una tarea por su id
        """
        data = self.list_tasks()

        if len(data) == 0:
            return {
                'message' : 'No se encontro la tarea'
            }

        task = list(filter(lambda task : task['id'] == id, data))

        if len(task) == 0:
            return {
                'message' : 'No se encontro la tarea'
            }

        return task[0]

        
    def _ultimo_id(self) -> int:
        """
        Obtiene el ultimo id de las tareas
        """
        data = self.list_tasks()
        
        id = len(data) + 1 
        return id

    def create_task(self , description:str , status:str = 'todo') -> dict:
        """
        Crea una tarea en el archivo json
        """

        data = self.list_tasks()

        id = self._ultimo_id

        task = Task(
            id = id,
            description = description,
            status = status,
            created_at = datetime.now().isoformat(),
            updated_at = None 
        )

        data.append(task.__dict__)

        json_manager.write_json(data)

        return task.__dict__
    

    def update_task(self, id:int, description:str) -> dict:
        """
        Actualiza una tarea
        """
        data = self.list_tasks()

        task = self.get_tast(id)

        if 'message' in task:
            return task
        
        task['description'] = description
        task['updated_at'] = datetime.now().isoformat()

        data = list(map(lambda x : task if x['id'] == id else x, data))

        json_manager.write_json(data)

        return task

    def update_status(self, id:int, status:str) -> dict:
        """
        Actualiza el status de una tarea
        """
        data = self.list_tasks()

        task = self.get_tast(id)

        if 'message' in task:
            return task
        
        task['status'] = status
        task['updated_at'] = datetime.now().isoformat()

        data = list(map(lambda x : task if x['id'] == id else x, data))

        json_manager.write_json(data)

        return task





        