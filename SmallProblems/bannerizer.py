
# Write a function that takes a short line of text and prints it within a box.

def bannerizer(message):
    message_length = len(message)
    print(f'+-{"-"*message_length}-+')
    print(f'| {" "*message_length} |')
    print(f'| {message} |')
    print(f'| {" "*message_length} |')
    print(f'+-{"-"*message_length}-+')

bannerizer('To boldly go where no one has gone before.')