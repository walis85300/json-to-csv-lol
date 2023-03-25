import typer
import json

from pathlib import Path
from typing import Optional

from .converter import convert as convert_json

app = typer.Typer()


def check_input(input: Path):
    """
    Check if the input file is a valid input
    """
    if not input.exists():
        print('File does not exist')
        raise typer.Abort()

    if not input.is_file():
        print('It is not a file')
        raise typer.Abort()

    if not input.suffix == '.json':
        print('It is not a json file')
        raise typer.Abort()


def check_output(path: Path):
    """
    Check is the output path is a valid dir
    """
    if not path.is_dir():
        print('Output path is not a dir')
        raise typer.Abort()


@app.command()
def convert(
    input_file: Path,
    output_path: Optional[Path] = typer.Option(Path('.')),
):
    """
    Convert the JSON file into a CSV
    """

    check_input(input_file)
    check_output(output_path)

    filename = input_file.stem
    filename = f'{filename}-converted.csv'

    output_file = output_path.joinpath(filename)
    output_file.touch(exist_ok=True)

    try:
        convert_json(input_file, output_file)
    except Exception as e:
        raise typer.Abort()

    print('Successfuly converted!')
