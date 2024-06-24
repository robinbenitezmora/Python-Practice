## Convert a json file into csv

This script take a json file as an input and generate a csv file in output

## Function Signature

```python

def convert_json_to_csv(input_file: str, output_file: str) -> None:

```

## Input

The input parameters are:

- `input_file`: a string representing the path to the input JSON file.

- `output_file`: a string representing the path to the output CSV file.

## Output

The function does not return any value. It converts the JSON file to a CSV file and saves it in the specified location.

## Constraints

- The input JSON file must exist and be valid.

- The output CSV file must not exist before running the script.

- The input JSON file must not be empty.

- The JSON file must contain a list of dictionaries.

- The dictionaries in the JSON file must have the same keys.

- The keys in the dictionaries must be strings.

- The values in the dictionaries must be strings, integers, or floats.

- The CSV file must contain a header row with the keys from the JSON file.

- The CSV file must contain one row for each dictionary in the JSON file.

- The CSV file must be saved in the specified location.

- The CSV file must be a valid CSV file.

- The CSV file must be readable by common spreadsheet software.

# How to run the script

To run the script, you need to provide the path to the input JSON file and the path to the output CSV file. The script will read the JSON file, convert it to a CSV file, and save it in the specified location.

You can run the script using the following command:

```bash

python convert_json_to_csv.py input.json output.csv

```

# Example

If the input JSON file `data.json` contains the following data:

```

[
  {
    "name": "Alice",
    "age": 25,
    "city": "New York"
  },
  {
    "name": "Bob",
    "age": 30,
    "city": "Los Angeles"
  },
  {
    "name": "Charlie",
    "age": 35,
    "city": "Chicago"
  }
]

```

After running the script with the following command:

```bash

python convert_json_to_csv.py data.json output.csv

```

The output CSV file `output.csv` will contain the following data:

```

name,age,city

Alice,25,New York

Bob,30,Los Angeles

Charlie,35,Chicago

```

The script will not print any output to the console.

# Requirements

- Python 3.x

- pandas library

You can install the pandas library using the following command:

```bash
