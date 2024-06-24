# Converter JPEG to PNG

This is a simple Python script that converts all the JPEG images in a folder to PNG images.

## How to use

1. Clone the repository

2. Run the script with the following command:

```bash
python converter.py
```

1. The script will convert all the JPEG images in the `images` folder to PNG images.

2. The converted images will be saved in the `output` folder.

3. The script will print the names of the converted images.

## Requirements

- Python 3.x

- Pillow library

You can install the Pillow library using the following command:

```bash
pip install Pillow
```

## Example

If the `images` folder contains the following JPEG images:

image1.jpg
image2.jpg
image3.jpg

After running the script, the `output` folder will contain the following PNG images:

image1.png
image2.png
image3.png

The script will print the following output:

```bash
Converting image1.jpg to image1.png
Converting image2.jpg to image2.png
Converting image3.jpg to image3.png
```

## Function Signature

```python

def convert_jpeg_to_png(input_folder: str, output_folder: str) -> None:

```

## Input

The input parameters are:

- `input_folder`: a string representing the path to the folder containing the JPEG images.

- `output_folder`: a string representing the path to the folder where the PNG images will be saved.

## Output

The function does not return any value. It converts all the JPEG images in the `input_folder` to PNG images and saves them in the `output_folder`.

## Constraints

- The input folders must exist and contain JPEG images.

- The output folder must exist and be empty.

- The input folders must not contain any PNG images.

- The input folders must not contain any other file types besides JPEG images.

- The input folders must not contain any subfolders.

- The input folders must not contain any hidden files.

- The input folders must not contain any files with the same name but different extensions.

- The input folders must not contain any files with the same name but different content.
