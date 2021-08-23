# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import json
from random import randrange

lives = 7
guesses = []
done = False

def guess_attempt():
    for letter in words:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

def lives_left():
    guess = input(f"Lives Left {lives}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in words.lower():
        lives -= 1
        if lives == 0:
            break
        
   
    done = True
    for letter in words:
        if letter.lower() not in guesses:
            done = False

def game_result():
    if done:
        print(f"Well done, you have won!  The word was {words}!")
    else:
        print(f"Game Over!  Better luck next time.  The word was {words}")


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
    print('Random word', get_random_word(selected_level, words_array))

    # Explains objectnavigation, you can delete
    # easy_array_length = len(words_array['easy']) - 1
    # random_index = randrange(easy_array_length)
    # print('Random easy word:', words_array['easy'][random_index])
    # print('Words easy: ', words_array['easy'][0])
    # print('Words medium: ', words_array['medium'][0])
    # print('Words hard: ', words_array['hard'][0])
