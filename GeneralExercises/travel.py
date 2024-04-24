
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def destination_list(city, destination_list):
    for destination in destination_list:
        if city == destination:
            return True
    return False

print(destination_list('Barcelona', destinations))  # True
print(destination_list('Nashville', destinations))  # False