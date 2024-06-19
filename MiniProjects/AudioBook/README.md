# Audiobook

## Description

This project is a simple audiobook that reads the text from a PDF file and plays it. It uses the PyPDF2 and pyttsx3 libraries.

### Install Requirements

```bash
pip install PyPDF2 pyttsx3
```

### Usage

```bash
python audiobook.py
```

### Author

[RBM]

### License

[MIT](https://choosealicense.com/licenses/mit/)

```

### audiobook.py[]: # Path: MiniProjects/AudioBook/audiobook.py
```python

import pyttsx3
import PyPDF2

# Open the PDF file
pdf = open('sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
pages = pdf_reader.numPages

# Initialize the speaker
speaker = pyttsx3.init()

# Read the text from the PDF file
for num in range(pages):
    page = pdf_reader.getPage(num)
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

# Close the PDF file
pdf.close()
```

### sample.pdf[]: # Path: MiniProjects/AudioBook/sample.pdf
