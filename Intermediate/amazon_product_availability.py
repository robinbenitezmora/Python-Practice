from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib

receiver_email_id = 'EMAIL_ID_OF_USER'

def check(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    for i in range(20):
        sleep(3)
        doc = html.fromstring(page.content)
        XPATH_AVAILABILITY = '//*[@id="availability"]//text()'
        RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
        AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
        return AVAILABILITY
    
def send_email(ans, product):
    GMAIL_USERNAME = 'YOUR_EMAIL_ID'
    GMAIL_PASSWORD = 'YOUR_EMAIL_PASSWORD'
    recipient = receiver_email_id
    body_of_email = 'Hey, the product you wanted is now available on Amazon. Here is the link: ' + ans
    email_subject = 'Your product is now available on Amazon'

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)

    headers = "\r\n".join(['from: ' + GMAIL_USERNAME,
                            'subject: ' + email_subject,
                            'to: ' + recipient,
                            'mime-version: 1.0',
                            'content-type: text/html'])
    
    content = headers + "\r\n\r\n" + body_of_email
    s.sendmail(GMAIL_USERNAME, recipient, content)
    s.quit()

def ReadAsin():
    # Asin Id is the product ID
    Asin = 'B07JGTVTWN'
    url = "https://www.amazon.in/dp/" + Asin

    # Comment the below line to enable the script
    print("Processing: " + url)
    ans = check(url)
    arr = [
        'Only 1 left in stock.',
        'Only 2 left in stock.',
        'In stock.'
    ]
    print(ans)
    if ans in arr:
        send_email(url, Asin)
        print('Email has been sent')
    else:
        print('Product is still not available')

def job():
    print("Tracking....")
    ReadAsin()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
