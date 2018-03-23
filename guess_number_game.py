import random

name = input('what is your name?')
print("Hello," + name + ".")
guessesTaken = 0
number = random.randint(1,20)
print("Well," + name + " I am thinking of a number between 1 and 20.")
for guessesTaken in range(6):
    print("Take a guess.")
    guess = input("Enter a number?")
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
        guessesTaken += 1

    if guess > number:
        print("Your guess is too high.")
        guessesTaken += 1

    if guess == number:
        print("Your guess is correct.")
        break
print("You figured out my number in " + str(guessesTaken) + " attempts.")
