# Write a program that asks the user for the weather and then gives them advice based on their input.
# Use a match statement to compare the weather variable to different cases.
weather = input('What is the weather like today?\n')

match weather:
    case 'rainy':
        print('Grab your umbrella!')
    case 'sunny':
        print('It is a beautiful day!')
    case 'snowy':
        print('Wear your boots!')
    case 'cloudy':
        print('It might rain, take your umbrella!')
    case _:
        print('Let\'s stay inside!')