
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue
    print(f'The city of {city} has {len(city)} characters.')