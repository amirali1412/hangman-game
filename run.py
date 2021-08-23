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


def game_result():
    if done:
        print(f"Well done, you have won!  The word was {words}!")
    else:
        print(f"Game Over!  Better luck next time.  The word was {words}")


def mask_current_word(word):
    masked = []
    for letter in word:
        masked.append('_')
    return ''.join(masked)


def validate_letter_in_word(letter, word):
    return letter.lower() in word.lower()


def get_letter_guess():
    letter = input(f"Input your guess: ")
    return letter


def update_masked_word(current_word, masked_word, current_letter):
    masked_word_array = list(masked_word)
    index = 0
    for letter in current_word:
        if letter.lower() == current_letter.lower():
            masked_word_array[index] = letter
        index += 1
    return ''.join(masked_word_array)


def play_word(current_word, masked_word, lives):
    while lives > -1:
        print('Challenge word: %s  Lives: %i' % (masked_word, lives))
        current_letter = get_letter_guess()
        if (validate_letter_in_word(current_letter, current_word)):
            print('Check if won')
        else:
            lives -= 1
        masked_word = update_masked_word(current_word, masked_word, current_letter)


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
    level = input(f"Select game level: Type 1- Easy, 2- Medium, 3- hard ")
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


if __name__ == '__main__':
    words_array = read_words_from_json_file()
    selected_level = select_game_level()
    current_word = get_random_word(selected_level, words_array)
    masked_word = mask_current_word(current_word)
    play_word(current_word, masked_word, lives)
