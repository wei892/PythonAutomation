import random

print("I'm thinking of a number between 1 and 20.")
print("Take a guess.")

secretNum =  random.randint(1, 20)
print(secretNum)
guessCount = 0
guess = input()

while int(guess) != secretNum:
    if int(guess) < secretNum:
        guessCount += 1
        print("Your guess is too low.")
        print("Take a guess")
    elif int(guess) > secretNum:
        guessCount += 1
        print("Your guess is too high.")
        print("Take a guess.")
    guess = input()

guessCount += 1
print("Good job! You guess my number in " + str(guessCount) + " guess!")