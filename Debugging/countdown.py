

# Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1.

def countdown():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("LAUNCH!")

countdown()
