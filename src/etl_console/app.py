import os
import sys
import click
sys.path.append(os.path.realpath(os.path.join(
    os.path.dirname(__file__), "..")))


@click.command()
@click.option("-f", "--file", required=True, type=str)
def run(file):
    from etl_core import loader
    df = loader.load(file)
    print(df)


if(__name__ == "__main__"):
    run()
