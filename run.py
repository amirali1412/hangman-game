# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import json
from random import randrange

lives = 7
guesses = []
done = False
masked_word = ''
current_word = ''


def game_result(user_won, word):
    if user_won:
        print(f"Well done, you have won!  The word was {word}!")
    else:
        print(f"Game Over!  Better luck next time.  The word was {word}")


def mask_current_word(word):
    masked = []
    for letter in word:
        masked.append('_')
    return ''.join(masked)


def validate_letter_in_word(letter, word):
    return letter.lower() in word.lower()


def get_letter_guess():
    retry_input_guess = True
    guess_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while retry_input_guess:
        letter = input(f"Input your guess:/n ")
        if letter.upper() in guess_options:
            if letter.upper() in guesses:
                print("You have already guessed that letter. Try again.")
            else:
                retry_input_guess = False
        else:
            print('You must enter an alphabetic character.')
    return letter


def update_masked_word(current_word, masked_word, current_letter):
    masked_word_array = list(masked_word)
    index = 0
    for letter in current_word:
        if letter.lower() == current_letter.lower():
            masked_word_array[index] = letter
        index += 1
    return ''.join(masked_word_array)


def check_if_user_won(current_word, masked_word):
    return masked_word.lower() == current_word.lower()


def play_word(current_word, masked_word, lives):
    user_won_game = False
    while (lives > 0) and (user_won_game is False):
        print('Challenge word: %s  Lives: %i' % (masked_word, lives))
        current_letter = get_letter_guess()
        guesses.append(current_letter.upper())
        if (validate_letter_in_word(current_letter, current_word)):
            masked_word = update_masked_word(current_word, masked_word, current_letter)
            user_won_game = check_if_user_won(current_word, masked_word)
        else:
            lives -= 1
    game_result(user_won_game, current_word)    


def read_words_from_json_file():
    try:
        file = open('./words.json','r')
        with file:
            return json.load(file)
        file.close()
    except IOError:
        return {}
    except ValueError:
        return {}
    except:
        raise


def select_game_level():
    retry_get_level = True
    level_options = ['1', '2', '3']
    while retry_get_level:
        level = input(f"Select game level: Type 1- Easy, 2- Medium, 3- hard ")
        if level in level_options:
            retry_get_level = False
        else:
            print('Please enter a valid option (1, 2 or 3)')
    return int(level)


def get_random_word(level, words_array):
    if level == 1:
        array_length = len(words_array['easy']) - 1
        level_key = 'easy'
    if level == 2:
        array_length = len(words_array['medium']) - 1
        level_key = 'medium'
    if level == 3:
        array_length = len(words_array['hard']) - 1
        level_key = 'hard'
    random_index = randrange(array_length)
    random_word = words_array[level_key][random_index]
    return random_word


def playAgain():
    retry_play_again = True
    available_options = ['N', 'Y', 'NO', 'YES']
    while retry_play_again:
        print('Do you want to play again? (yes or no)')
        option = input().upper()
        if option in available_options:
            retry_play_again = False
    return option.startswith('Y')


if __name__ == '__main__':
    words_array = read_words_from_json_file()
    play_game = True
    while play_game:
        selected_level = select_game_level()
        current_word = get_random_word(selected_level, words_array)
        masked_word = mask_current_word(current_word)
        play_word(current_word, masked_word, lives)
        lives = 7
        guesses = []
        play_game = playAgain()
    print('Thank you for playing')