from gtts import gTTS

import PyPDF2

pdf_File = open('name.pdf', 'rb')

pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf.Reader.numPages
textList = []

for i in range(count):
    try:
        page = pdf_Reader.getPage(i)
        textList.append(page.extractText())
    except:
        pass

textStr = ' '.join(textList)

print(textStr)

language = 'en'

audio = gTTS(text=textStr, lang=language, slow=False)

audio.save('audio.mp3')
