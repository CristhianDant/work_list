from tabulate import tabulate

class PrintTabulate:
    def __init__(self , tableformat:str = "pretty"):
        self.tableformat = tableformat
    
    def print_table_list(self, data:list) -> str:
        """
        Imprime los datos en forma de tabla
        """
        
        return print(
            tabulate(
                data,
                headers="keys",
                tablefmt=self.tableformat
            )
        )

    def print_table_dict(self, data:dict) -> str:
        """
        Imprime los datos en forma de tabla
        """
        
        return print(
            tabulate(
                [data],
                headers="keys",
                tablefmt=self.tableformat
            )
        )