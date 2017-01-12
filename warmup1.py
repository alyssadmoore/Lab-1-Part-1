import random

number = random.randint(1, 10)

# for testing
print(number)

while True:
    guess = int(input("Guess a number between 1 and 10.\n"))
    if guess < number:
        print("Higher!")
    if guess > number:
        print("Lower!")
    if guess == number:
        print("Correct!")
        break
