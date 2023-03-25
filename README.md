# json-to-csv-lol

`json-to-csv-lol` is a Python command line interface (CLI) tool that allows you to convert JSON files to CSV format.

## Prerequisites

json-to-csv-lol requires the following to be installed on your system:

    Python 3.10 or higher
    pip package manager

## Installation

To install `json-to-csv-lol`, you can use `pip`. Open up a terminal and run:

```bash
pip install json-to-csv-lol
```


## Usage

Once you have installed `json-to-csv-lol`, you can use it from the command line. The tool accepts a path to a valid JSON file and an optional output path to write the resulting CSV file.

To use the tool, open a terminal and run:

```bash
json-to-csv-lol input_path.json --output-path output_dir/
```


Where `input_path.json` is the path to the input JSON file and `output_dir/` is the directory where the resulting CSV file should be saved.

If the `--output-path` option is not provided, the tool will save the resulting CSV file in the same directory as the input JSON file with the same filename, but with a .csv extension.

## Example

To convert a data.json file to a CSV file and save it in a csv directory, run:

```bash
json-to-csv-lol data.json --output-path csv/
```


## Contributing

If you find any bugs or would like to contribute to the development of `json-to-csv-lol`, please feel free to open an issue or pull request on the GitHub repository.

## License

`json-to-csv-lol` is licensed under the MIT License.
