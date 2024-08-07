import random, shutil, sys, time

PAUSE = 0.15
DENSITY = 0.10

DUCKLING_WIDTH = 10
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

DUCKLING = {
    'head': {
        'left': {
            'beady': '   .-.',
            'wide': '  .-.'
        },
        'right': {
            'beady': '.-.   ',
            'wide': '.-.  '
        }
    },
    'body': {
        'happy': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'aloof': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'chubby': {
            'left': ' (o o)',
            'right': '( o o)'
        },
        'very chubby': {
            'left': ' (o o)',
            'right': '( o o)'
        }
    },
    'feet': {
        'open': {
            'left': '  J J',
            'right': 'J J  '
        },
        'closed': {
            'left': '  " "',
            'right': '" "  '
        }
    }
}

try:
    print('Duckling Animation, press Ctrl-C to quit...')
    print('Press Ctrl-C to quit.')
    time.sleep(2)
    rowIndex = 0

    while True:
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            if (ducklingObj == None) or (random.random() > DENSITY):
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                print(ducklingObj.getLaneStr(laneNum), end='')
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                print(' ' * DUCKLING_WIDTH, end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        headStr = ''
        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'
            headStr += ') '

        if self.direction == RIGHT:
            headStr += ' ('
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:
            headStr += ' '

        return headStr
    
    def getBodyStr(self):
        bodyStr = ' ('
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:

        if self.direction == RIGHT:
            if self.wing == DOWN:
                bodyStr += 'v'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == OUT:
                bodyStr += '<'

            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        if self.body == CHUBBY:
            bodyStr += ' '
        return bodyStr
    
    def getFeetStr(self):
        if self.body == CHUBBY:
            return '  " "'
        elif self.body == VERY_CHUBBY:
            return ' " " '
        
    def getNextBodyPart(self):
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
 