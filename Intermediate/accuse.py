import time, random, sys

SUSPECTS = ['Miss Scarlet', 'Col. Mustard', 'Mrs. White', 'Mr. Green', 'Mrs. Peacock', 'Prof. Plum']
ITEMS = ['Candlestick', 'Knife', 'Lead Pipe', 'Revolver', 'Rope', 'Wrench']
PLACES = ['Kitchen', 'Ballroom', 'Conservatory', 'Dining Room', 'Library', 'Lounge', 'Hall', 'Study', 'Billiard Room']
TIME_TO_SOLVE = 300

PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0].lower()] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

assert len(SUSPECTS) == 6
assert len(ITEMS) == 6
assert len(PLACES) == 9
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

knownSuspectsAndItems = []
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspect = []
liars = random.sample(SUSPECTS, random.randint(1, 5))
accusationLeft = 3
culprit = random.choice(SUSPECTS)

random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        clues[interviewee] = {}
        clues[interviewee]['suspect'] = random.choice(SUSPECTS)
        clues[interviewee]['item'] = random.choice(ITEMS)
        clues[interviewee]['place'] = random.choice(PLACES)
    else:
        clues[interviewee] = {}
        clues[interviewee]['suspect'] = culprit
        clues[interviewee]['item'] = random.choice(ITEMS)
        clues[interviewee]['place'] = random.choice(PLACES)

def printClues():
    for suspect in clues:
        print(f"{suspect} says: {clues[suspect]['suspect']} did it with the {clues[suspect]['item']} in the {clues[suspect]['place']}")
    print()

def printKnownSuspectsAndItems():
    print("Known Suspects and Items:")
    for suspect, item in knownSuspectsAndItems:
        print(f"{suspect} has the {item}")
    print()

def printVisitedPlaces():
    print("Visited Places:")
    for place in visitedPlaces:
        print(place)
    print()

def printCurrentLocation():
    print(f"Current Location: {currentLocation}")
    print()

def printAccusedSuspect():
    print(f"Accused Suspect: {accusedSuspect}")
    print()

def printLiars():
    print("Liars:")
    for liar in liars:
        print(liar)
    print()

def printAccusationLeft():
    print(f"Accusation Left: {accusationLeft}")
    print()

def printCulprit():
    print(f"Culprit: {culprit}")
    print()

def printAll():
    printClues()
    printKnownSuspectsAndItems()
    printVisitedPlaces()
    printCurrentLocation()
    printAccusedSuspect()
    printLiars()
    printAccusationLeft()
    printCulprit()

def printHelp():
    print("Commands:")
    print("  - 'clues': print all clues")
    print("  - 'known': print known suspects and items")
    print("  - 'visited': print visited places")
    print("  - 'location': print current location")
    print("  - 'accused': print accused suspect")
    print("  - 'liars': print liars")
    print("  - 'accusation': print accusation left")
    print("  - 'culprit': print culprit")
    print("  - 'all': print all")
    print("  - 'help': print this help message")
    print("  - 'exit': exit the game")
    print()

def printIntro():
    print("Welcome to Clue!")
    print("You are a detective trying to solve a case.")
    print("You have 3 chances to accuse the suspect.")
    print("You can ask each suspect for a clue.")
    print("Good luck!")
    print()

def printOutro():
    print("Game Over!")
    print(f"The culprit is {culprit}")
    print()

def printInvalidCommand():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidPlace():
    print("Invalid place. Type 'visited' to see the list of visited places.")
    print()

def printInvalidSuspect():
    print("Invalid suspect. Type 'known' to see the list of known suspects and items.")
    print()

def printInvalidItem():
    print("Invalid item. Type 'known' to see the list of known suspects and items.")
    print()

def printInvalidAccusation():
    print("Invalid accusation. You need to accuse a suspect.")
    print()

def printInvalidAccusationLeft():
    print("Invalid accusation left. You have no accusation left.")
    print()

def printInvalidLocation():
    print("Invalid location. You need to be in a place to accuse a suspect.")
    print()

def printInvalidLiars():
    print("Invalid liars. You need to be in a place to accuse a suspect.")
    print()

def printInvalidCulprit():
    print("Invalid culprit. You need to be in a place to accuse a suspect.")
    print()

def printInvalidClue():
    print("Invalid clue. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidClues():
    print("Invalid clues. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidKnownSuspectsAndItems():
    print("Invalid known suspects and items. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidVisitedPlaces():
    print("Invalid visited places. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidCurrentLocation():
    print("Invalid current location. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidAccusedSuspect():
    print("Invalid accused suspect. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidHelp():
    print("Invalid help. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidAll():
    print("Invalid all. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidExit():
    print("Invalid exit. You need to be in a place to ask a suspect for a clue.")
    print()

def printInvalidCommandInPlace():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInAccused():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInLiars():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInAccusationLeft():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInCulprit():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInClue():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInClues():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInKnownSuspectsAndItems():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInVisitedPlaces():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInCurrentLocation():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInHelp():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInAll():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInExit():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInInvalidPlace():
    print("Invalid command. Type 'help' for a list of commands.")
    print()

def printInvalidCommandInInvalidSuspect():
    print("Invalid command. Type 'help' for a list of commands.")
    print()
    