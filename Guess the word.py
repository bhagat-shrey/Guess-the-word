

import random

wordList = ["Apple", "Banana", "Cat", "Dog", "Elephant"]
word = random.choice(wordList).lower()  # Convert the chosen word to lowercase
print(word)

endOfGame = False
guessed_letters = set()  # Keep track of guessed letters

while not endOfGame:
    userInput = input("Guess a letter: ").lower()

    if userInput in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.add(userInput)

    newLetter = ""
    for char in word:
        if char in guessed_letters:
            newLetter += char
        else:
            newLetter += "_"

    print(newLetter)

    if "_" not in newLetter:
        endOfGame = True
        print("You win!")


# print(newLetter)