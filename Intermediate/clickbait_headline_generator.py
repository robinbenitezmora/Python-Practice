import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them', 'Us', 'Me', 'You']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their', 'Our', 'My', 'Your']
PERSONAL_PRONOUNS = ['She', 'He', 'They', 'We', 'I', 'You']
STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

NOUNS = ['Cat', 'Dog', 'Person', 'Place', 'Thing', 'Food', 'Animal', 'Plant', 'Car', 'Book', 'Movie', 'Song', 'Game', 'Website', 'Computer', 'Phone', 'Tablet', 'Headphone', 'Speaker', 'Shoe', 'Hat', 'Shirt', 'Pants', 'Dress', 'Jacket', 'Socks', 'Underwear', 'Towel', 'Blanket', 'Pillow', 'Bed', 'Couch', 'Chair', 'Table', 'Desk', 'Lamp', 'Clock', 'Watch', 'Ring', 'Bracelet', 'Necklace', 'Earring', 'Glasses', 'Sunglasses', 'Belt', 'Wallet', 'Purse', 'Bag', 'Backpack', 'Suitcase', 'Umbrella', 'Key', 'Lock', 'Knife', 'Spoon', 'Fork', 'Bowl', 'Plate', 'Cup', 'Glass', 'Mug', 'Bottle', 'Box', 'Bag', 'Basket', 'Cart', 'Truck', 'Bus', 'Bike', 'Motorcycle', 'Airplane', 'Boat', 'Train', 'Subway', 'Taxi', 'Car', 'Truck', 'Van', 'SUV', 'Jeep', 'Convertible', 'Sedan', 'Coupe', 'Hatchback', 'Minivan', 'Pickup', 'Station Wagon', 'Limousine', 'RV', 'Motorcycle', 'Scooter', 'Moped', 'Dirt Bike', 'ATV', 'Snowmobile', 'Jet Ski', 'Bicycle', 'Tricycle', 'Unicycle', 'Penny Farthing', 'Segway', 'Hoverboard', 'Roller Skates', 'Roller Blades', 'Ice Skates', 'Skateboard', 'Longboard', 'Surfboard', 'Paddleboard', 'Wakeboard', 'Kiteboard', 'Snowboard', 'Ski', 'Sled', 'Toboggan', 'Snow Tube', 'Snowshoe', 'Ice Skate', 'Hockey Skate', 'Figure Skate', 'Speed Skate', 'Inline Skate', 'Roller Skate', 'Roller Blade', 'Ice Hockey Skate', 'Figure Skating Skate', 'Speed Skating Skate', 'Inline']

PLACES = ['House', 'School', 'Store', 'Restaurant', 'Park', 'Zoo', 'Mall', 'Library', 'Gym', 'Pool', 'Beach', 'Lake', 'River', 'Ocean', 'Sea', 'Mountain', 'Hill', 'Valley', 'Cave', 'Forest', 'Jungle', 'Desert', 'Tundra', 'Swamp', 'Marsh', 'Field', 'Farm', 'Garden', 'Orchard', 'Vineyard', 'Pasture', 'Prairie', 'Plains', 'Savanna', 'Rainforest', 'Wetland', 'Beach', 'Coast', 'Shore', 'Cliff', 'Canyon', 'Waterfall', 'Volcano', 'Geyser', 'Hot Spring', 'Glacier', 'Iceberg', 'Ice Shelf', 'Ice Sheet', 'Ice Cap', 'Ice Field', 'Ice Floe', 'Ice Pack', 'Iceberg', 'Ice Shelf', 'Ice Sheet', 'Ice Cap', 'Ice Field', 'Ice Floe', 'Ice Pack', 'Island', 'Peninsula', 'Isthmus', 'Archipelago', 'Atoll', 'Cay', 'Coral Reef', 'Lagoon', 'Bay', 'Gulf', 'Strait', 'Sound', 'Channel', 'Fjord', 'Inlet', 'Harbor', 'Port', 'Dock', 'Marina', 'Wharf', 'Pier', 'Quay', 'Jetty', 'Breakwater', 'Seawall', 'Lighthouse', 'Buoy', 'Beacon', 'Barge', 'Boat', 'Ship', 'Yacht', 'Sailboat', 'Sail', 'Mast', 'Hull', 'Deck', 'Cabin', 'Cockpit', 'Rudder', 'Keel', 'Anchor', 'Rope', 'Line', 'Chain', 'Sail', 'Mast', 'Hull', 'Deck', 'Cabin', 'Cockpit', 'Rudder', 'Keel', 'Anchor', 'Rope', 'Line', 'Chain', 'Cruise Ship', 'Ferry', 'Cargo Ship', 'Tanker', 'Container Ship', 'Battleship', 'Aircraft Carrier', 'Submarine', 'Oil Rig', 'Drilling Platform', 'Drilling Rig']

WHEN = ['Soon', 'Later', 'Tomorrow', 'Today', 'Yesterday', 'Now']

def main():
    print('Clickbait Headline Generator')

    while True:
        print()
        print('Enter "exit" to quit.')
        respone = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadLines):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillenialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowAboutHeadline()
        elif clickbaitType == 3:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 4:
            headline = generateXOfTheBestHeadline()
        elif clickbaitType == 5:
            headline = generateXReasonsWhyHeadline()
        elif clickbaitType == 6:
            headline = generateXSecretsOfHeadline()
        elif clickbaitType == 7:
            headline = generateXThingsYouHeadline()
        elif clickbaitType == 8:
            headline = generateXWaysToHeadline()

        print(headline)
    print()

    website = random.choice('website', 'blog', 'social media', 'online store', 'forum', 'webcomic', 'webzine', 'webseries', 'webshow', 'webcast', 'webinar', 'weblog', 'vlog', 'podcast', 'webpage', 'webapp', 'webgame', 'webforum', 'webcomic', 'webzine', 'webseries', 'webshow', 'webcast', 'webinar', 'weblog', 'vlog', 'podcast', 'webpage', 'webapp', 'webgame', 'webforum')

    when = random.choice(WHEN).lower()
    print('Published on {} at {}'.format(website, when))

def generateAreMillenialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)

def generateWhatYouDontKnowAboutHeadline():
    noun = random.choice(NOUNS)
    return 'What You Dont Know About the {} Industry Could Fill a Book'.format(noun)

def generateYouWontBelieveHeadline():
    noun = random.choice(NOUNS)
    return 'You Wont Believe What This {} Looks Like Now'.format(noun)

def generateXOfTheBestHeadline():
    noun = random.choice(NOUNS)
    return 'X of the Best {}s You Can Buy'.format(noun)

def generateXReasonsWhyHeadline():
    noun = random.choice(NOUNS)
    return 'X Reasons Why You Should Buy a {}'.format(noun)

def generateXSecretsOfHeadline():
    noun = random.choice(NOUNS)
    return 'X Secrets of the {} Industry'.format(noun)

def generateXThingsYouHeadline():
    noun = random.choice(NOUNS)
    return 'X Things You Didnt Know About {}'.format(noun)

def generateXWaysToHeadline():
    noun = random.choice(NOUNS)
    return 'X Ways to Improve Your {}'.format(noun)

if __name__ == '__main__':
    main()
    