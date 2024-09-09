import random, sys

QUESTIONS = [
    {'question': 'How many times can you subtract 5 from 25?', 'answer': 'Once, then you have a pile of 20.'},
    {'question': 'What has keys but can\'t open locks?', 'answer': 'A piano.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
    {'question': 'What has a neck but no head?', 'answer': 'A bottle.'},
    {'question': 'What has a thumb and four fingers but is not a hand?', 'answer': 'A glove.'},
    {'question': 'What has a single eye but cannot see?', 'answer': 'A needle.'},
    {'question': 'What has a foot but no legs?', 'answer': 'A ruler.'},
    {'question': 'What has a heart that doesn\'t beat?', 'answer': 'An artichoke.'},
    {'question': 'What has a bed but never sleeps?', 'answer': 'A river.'},
    {'question': 'What has a face and two hands but no arms or legs?', 'answer': 'A clock.'},
    {'question': 'What has a head, a tail, is brown, and has no legs?', 'answer': 'A penny.'},
]

CORRECT_TEXT = 'Correct! The answer is: {}'
INCORRECT_TEXT = 'Incorrect! The answer is: {}'

input("Press ENTER to start the quiz...")
random.shuffle(QUESTIONS)
score = 0

for questionNumber, qa in enumerate(QUESTIONS, 1):
    print(f"Question {questionNumber}: {qa['question']}")
    answer = input("Enter your answer: ")
    if answer.lower() == qa['answer'].lower():
        print(CORRECT_TEXT.format(qa['answer']))
        score += 1
    else:
        print(INCORRECT_TEXT.format(qa['answer']))

print(f"Your final score is {score}/{len(QUESTIONS)}")
print("Thanks for playing!")
sys.exit(0)

# The code snippet above is a quiz game that asks the user trick questions. The questions and answers are stored in a list of dictionaries. The program shuffles the questions and then asks the user each question in order. The user's input is compared to the correct answer, and the score is calculated based on the number of correct answers. Finally, the program prints the user's final score and exits.
