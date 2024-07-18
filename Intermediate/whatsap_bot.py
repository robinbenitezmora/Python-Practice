from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse # type: ignore
import requests
import json

app = Flask(__name__)

@app.route('/bot', methods=['POST'])

def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'quote' in incoming_msg:
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True

    if 'cat' in incoming_msg:
        r = requests.get('https://aws.random.cat/meow')
        if r.status_code == 200:
            data = r.json()
            cat = data['file']
        else:
            cat = 'I could not retrieve a cat image at this time, sorry.'
        msg.media(cat)
        responded = True

    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')

    return str(resp)

if __name__ == '__main__':
    app.run()
    