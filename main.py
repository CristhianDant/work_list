import typer
from typing_extensions import Annotated

from models.task_servise import Task_service
from models.print_tabulate import PrintTabulate


app = typer.Typer(no_args_is_help=True)
task_service = Task_service()
print_tabulate = PrintTabulate()

@app.command()
def listTask():
    """
    Lista todas las tareas
    """
    data = task_service.list_tasks()
    print_tabulate.print_table_list(data)

@app.command()
def task(
    id:int = typer.Argument(
        default=1,
        help="Id de la tarea"
    )):
    """
    Obtiene una tarea por su id
    """
    task = task_service.get_tast(id)
    print_tabulate.print_table_dict(task)

@app.command()
def createTask(
    description:str = typer.Argument(
        default="",
        help="Descripcion de la tarea"
    )):
    """
    Crea una tarea en el archivo json
    """
    task = task_service.create_task(description)
    print_tabulate.print_table_dict(task)

@app.command()
def updateTask(
    id:int = typer.Argument(
        default=1,
        help="Id de la tarea"
    ),
    description:str = typer.Argument(
        default="",
        help="Descripcion de la tarea"
    )):
    """
    Actualiza una tarea en el archivo json
    """
    task = task_service.update_task(id, description)
    print_tabulate.print_table_dict(task)

@app.command()
def updateStatus(
    id:int = typer.Argument(
        default=0,
        help="Id de la tarea"
    ),
    status: Annotated[int, typer.Option(help="Estado de la tarea")] = 0):
    """
    Actualiza el estado de una tarea en el archivo json
    """
    if status == 0:
        print("Debe ingresar un estado")
        raise typer.Abort()
    elif status == 1:
        status = "todo"
        task = task_service.update_status(id, status)
    elif status == 2:
        status = "in-progress"
        task = task_service.update_status(id, status)
    elif status == 3:
        status = "done"
        task = task_service.update_status(id, status)
    else:
        print("El estado ingresado no es valido")
        raise typer.Abort()

    print_tabulate.print_table_dict(task)

if __name__ == "__main__":
    app()
    
