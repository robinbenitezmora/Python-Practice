'''
Progress Bar Simulation using Python Tqdm Module 
'''

import random, time

BAR = chr(9608)

def progress_bar(iterable, length=50):
    total = len(iterable)
    for i, item in enumerate(iterable, 1):
        progress = BAR * int(i / total * length)
        spaces = ' ' * (length - len(progress))
        print(f'\rProgress: |{progress}{spaces}| {i}/{total}', end='', flush=True)
        yield item

def main():
    print('Progress Bar Simulation')
    items = list(range(1, 101))
    for _ in progress_bar(items):
        time.sleep(random.uniform(0.1, 0.5))
    print('\nSimulation complete')

if __name__ == '__main__':
    main()
    