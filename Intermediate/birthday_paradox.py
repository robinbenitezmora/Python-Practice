import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA
    return None

def main():
    print('''Birthday Paradox
    The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly high.
    This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.
    It generates N random birthdays and checks for a birthday match.
    ''')
    numberOfBirthdays = 100
    numberofMatches = 0
    for i in range(100):
        birthdays = getBirthdays(numberOfBirthdays)
        match = getMatch(birthdays)
        if match != None:
            numberofMatches += 1
    print('{} matches in {} simulations'.format(numberofMatches, 100))

if __name__ == '__main__':
    main()
# What is the output of the following code?

# A) 0 matches in 100 simulations
# B) 1 matches in 100 simulations
# C) 2 matches in 100 simulations
# D) 3 matches in 100 simulations

# Correct Answer: C) 2 matches in 100 simulations

# Explanation: The code simulates 100 groups of 100 people and checks if any two people in the group have the same birthday. The getBirthdays() function generates a list of random birthdays, and the getMatch() function returns the first matching birthday it finds. The main() function runs the simulation 100 times and counts the number of matches. Since the Birthday Paradox states that there is a high probability of two people sharing a birthday in a group of 23 or more people, it is expected that there will be multiple matches in the simulation. In this case, the output is "2 matches in 100 simulations", indicating that there were 2 instances of matching birthdays in the 100 groups of 100 people.
# The correct answer is C) 2 matches in 100 simulations.
# The code is a Monte Carlo simulation of the Birthday Paradox, which shows that the probability of two people sharing a birthday is higher than expected in a group of a certain size. The code generates random birthdays for a group of people and checks for matches. It then runs the simulation multiple times to determine the frequency of matches. In this case, there were 2 matches in 100 simulations.