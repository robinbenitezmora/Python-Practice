
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
character = input('Enter a character: ')

def contain_character(sequence, character):
    return character in sequence

print(contain_character(char_sequence, character))