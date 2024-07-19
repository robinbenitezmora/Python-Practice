def manage_queue(queue, action, *args):
    if action == 'add':
        queue.append(args[0])
    elif action == 'remove':
        queue.pop(0)
    elif action == 'print':
        print(queue)
    else:
        print('Invalid action')

queue = []
manage_queue(queue, 'add', 1)
manage_queue(queue, 'add', 2)
manage_queue(queue, 'add', 3)
manage_queue(queue, 'print')
manage_queue(queue, 'remove')
manage_queue(queue, 'print')

    