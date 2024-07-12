import hashlib
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file('Beginner/fun_fact_generator_web_app.py', 'Beginner/check_match_pdf.py')

if msg1 == msg2:
    print('The files are the same.')
else:
    print('The files are different.')