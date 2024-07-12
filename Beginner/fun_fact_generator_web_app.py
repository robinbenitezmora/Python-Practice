import json
import requests
from pywebio.input import input, select
from pywebio.output import put_text, put_buttons, put_image, put_html, style
from pywebio.session import hold, clear

def get_fun_fact():
    clear()

    put_html(
        '<p align="left">'
        '<h2><img src="https://www.pngitem.com/pimgs/m/146-1468479_fun-facts-png-transparent-png.png" alt="Fun Facts" width="100" height="100"> Fun Facts Generator</h2>'
        '</p>'
    )

    url = 'https://uselessfacts.jsph.pl/random.json?language=en'

    response = requests.get(url)
    data = json.loads(response.text)

    useless_fact = data['text']

    style(put_text(useless_fact), 'color: blue; font-size: 20px;')

    put_buttons([dict(label='Click me', value='outline-success', color='outline-success')], onclick=get_fun_fact)
    hold()

if __name__ == '__main__':
    get_fun_fact()
