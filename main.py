from category import get_category
from word import get_word
from difficulty import easy, medium, hard

def main():
    print('''
            !!!Welcome to H A N G M A N!!!      
    ''')

    print('So let\'s start')
    secret_word = get_word(get_category())

    hidden = []
    missed_letters = []
    guessed_letters = []

    for _ in range(len(secret_word.strip())):
        hidden.append('_')

    level_of_difficulty = input('Choice level of diffuclty: EASY , MEDIUM, HARD: ').lower()
    print(f'Difficult is {level_of_difficulty}', end='\n\n')
    if level_of_difficulty == 'easy':
        lvl = easy
    if level_of_difficulty == 'medium':
        lvl = medium
    if level_of_difficulty == 'hard':
        lvl = hard

    index = None
    index_lvl = 0
    tries = len(lvl) - 1

    while tries != 0 and '_' in hidden:
        print(f'You have {tries} tries')
        print(lvl[index_lvl])
        print(f'Guessed letters: {guessed_letters}', end='\n\n')
        print(f'Missed letters: {missed_letters}', end='\n\n')
        print('The hidden word -->', ' '.join(hidden), end='\n\n')
        letter = input('Enter a letter: ').lower()

        if len(letter) == 1 and letter in 'abcdefjhigklmnopqrstuvwxyz':
            if letter in secret_word.lower() and letter not in guessed_letters:
                if secret_word.lower().count(letter) == 1:
                    index = secret_word.lower().find(letter)
                    hidden[index] = letter
                    guessed_letters.append(letter)
                else:
                    start = -1
                    index_arr = []
                    while True:
                        try:
                            i = secret_word.lower().index(letter, start + 1)
                        except ValueError:
                            break
                        else:
                            index_arr.append(i)
                            start = i
                    for i in index_arr:
                        hidden[i] = letter
            else:
                tries -= 1
                index_lvl += 1
                missed_letters.append(letter)
        else:
            print("Wrong symbol, try again!")

    hidden = ''.join(hidden)

    if tries == 0:
        print(lvl[index_lvl])
        print('You lose, the word is', secret_word.upper())
    else:
        print('Right, it\'s', hidden.upper(), end='\n\n')


if __name__ == '__main__':
    main()

    again = input('Play again? Y/N: ')
    if again == 'y':
        main()
    else:
        print('''
            Goodbye!        
        ''')