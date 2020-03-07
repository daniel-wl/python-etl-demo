import click


@click.command()
@click.option("-f", "--file", required=True, type=str)
def run(file):
    print(f"Hello, {file}!")


if(__name__ == "__main__"):
    run()
