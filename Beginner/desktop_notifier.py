'''
How to play desktop notifier game:
1. Enter the title and message for the notification
2. The notification will be displayed on the desktop
3. The game ends after displaying the notification
'''

import requests
from plyer import notification

def get_quote():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
        return f'{quote} - {author}'
    return 'Unable to retrieve quote'

def display_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Desktop Notifier',
        timeout=10
    )

def main():
    title = input('Enter the title for the notification:\n')
    message = input('Enter the message for the notification:\n')
    display_notification(title, message)
    print('Notification displayed successfully!')

if __name__ == '__main__':
    main()