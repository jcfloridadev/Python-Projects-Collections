lowerBound = int(input("Enter the lower bound: "))
upperBound = int(input("Enter the upper bound: "))

while lowerBound >= upperBound:
    print("Lower bound must be less than upper bound.")
    lowerBound = int(input("Enter the lower bound: "))
    upperBound = int(input("Enter the upper bound: "))

secretNumber = random.randint(lowerBound, upperBound)

guessedCorrectly = False

while guessedCorrectly is False:

    userGuess = int(input("Guess a number between the bounds: "))

    while userGuess < lowerBound or userGuess > upperBound:
        userGuess = int(input("Invalid guess. Must be within the bounds: "))

    if userGuess < secretNumber:
        print("Too low")
    elif userGuess > secretNumber:
        print("Too high")
    else:
        print("Correct! You guessed the number.")
        guessedCorrectly = True

print("Thanks for playing!")