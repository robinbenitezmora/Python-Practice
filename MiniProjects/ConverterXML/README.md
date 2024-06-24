# Converter

This is a simple Python script that converts all the XML files in a folder to JSON files.

## How to use

1. Clone the repository

1. Run the script with the following command:

```bash

python converter.py
```

1. The script will convert all the XML files in the `xml` folder to JSON files.

2. The converted files will be saved in the `json` folder.

5. The script will print the names of the converted files.

## Requirements

- Python 3.x

- xmltodict library

You can install the xmltodict library using the following command:

```bash
pip install xmltodict
```

## Example

If the `xml` folder contains the following XML files:

data1.xml
data2.xml
data3.xml

After running the script, the `json` folder will contain the following JSON files:

data1.json
data2.json
data3.json

The script will print the following output:

```bash

Converting data1.xml to data1.json

Converting data2.xml to data2.json

Converting data3.xml to data3.json
```
