'''
How to play Flames game:
1. Enter your name and your partner's name
2. Remove all the common characters in both names
3. Count the total number of characters that are left
4. Find the word 'FLAMES' and remove the letter that corresponds to the total number of characters
5. The remaining letter will be the result of the game
'''

def flames_game(name1, name2):
    # Remove common characters in both names
    name1 = name1.lower()
    name2 = name2.lower()
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    # Count the total number of characters left
    total_chars = len(name1) + len(name2)
    # Find the word 'FLAMES'
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    while len(flames) > 1:
        index = total_chars % len(flames) - 1
        if index >= 0:
            flames = flames[index + 1:] + flames[:index]
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]
