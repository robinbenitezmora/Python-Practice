import sys
import im2pdf
import os

filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open('output.pdf', 'wb') as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith('.jpg'):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(im2pdf.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith('.jpg'):
        with open('output.pdf', 'wb') as f:
            f.write(im2pdf.convert(filepath))
else:
    print("Invalid file or directory")

