greet = input('Enter your language in order to greet you:\n')

def greet_match(greet_languge):
    match greet_languge:
        case 'en':
            return f'Hello!'
        case 'fr':
            return f'Salut!'
        case 'pt':
            return f'Ola!'
        case 'de':
            return f'Hallo!'
        case 'sv':
            return f'Hej!'
        case 'es':
            return f'Hola!'
        case 'it':
            return f'Ciao!'
        case 'nl':
            return f'Hallo!'
        case 'ru':
            return f'Privet!'
        case _ :
            return f'I\'m sorry, I don\'t know that language.'

greet_match(greet)