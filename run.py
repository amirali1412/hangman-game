# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

words_easy = ["happy", "table", "books", "extra", "queen", "apple", "fairy", "yacht", "prince", "joker"]

lives = 7
guesses = []
done = False

while not done:
    for letter in words_easy:
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Lives Left {lives}, Next Guess: ")
    guesses.append(guess.upper())
    if guess.upper() not in words_easy.upper():
        lives -= 1
        if lives == 0:
            break
    
    done = True
    for letter in words_easy:
        if letter.upper() not in guesses:
            done = False

if done:
    print(f"Well done, you have won!  The word was {words_easy}!")
else:
    print(f"Game Over!  The word was {words_easy}")

