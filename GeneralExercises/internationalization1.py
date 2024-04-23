greet = input('Enter your language in order to greet you:\n')

def greet_match(greet):
    match greet:
        case 'en':
            print('Hi!')
        case 'fr':
            print('Salut!')
        case 'pt':
            print('Olá!')
        case 'de':
            print('Hallo!')
        case 'sv':
            print('Hej!')
        case 'es':
            print('Hola!')
        case 'it':
            print('Ciao!')
        case 'nl':
            print('Hallo!')
        case 'ru':
            print('Privet!')
        case _ :
            print('Sorry, I do not speak that language.')

greet_match(greet)