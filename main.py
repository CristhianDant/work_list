import typer


app = typer.Typer()

@app.command()
def hello(name: str = typer.Argument(default="Cristhin ", help="The name to say hello to")):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()