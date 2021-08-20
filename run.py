# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

words_easy = ["happy", "table", "books", "extra", "queen", "apple", "fairy", "yacht", "prince", "joker"]

lives = 7
guesses []
done = False

while not done:
    for letter in word:
        if letter.upper() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    done=True

guess = input(f"Lives Left {lives}, Next Guess: ")

