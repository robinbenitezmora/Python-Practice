import imaplib, email

user = 'USER_EMAIL_ADDRESS'
password = 'USER_EMAIL_PASSWORD'
imap_url = 'imap.gmail.com'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
    
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('Inbox')

msg = get_emails(search('FROM', 'SENDER_EMAIL_ADDRESS', con))

for msgs in msg[::-1]:
    for sent in msg:
        if type(sent) is tuple:
            content = str(sent[1], 'utf-8')
            data = str(content)
            
            try:
                indexstart = data.find('ltr')
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find('</div>')

                print(data2[0: indexend])
            except UnicodeEncodeError as e:
                pass
            except IndexError as e:
                pass
            except Exception as e:
                print(e)

con.logout()
