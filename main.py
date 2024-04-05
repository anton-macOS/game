from random import choice

# word = ['apple', 'orange', 'pineapple', 'watermelon', 'melon', 'grape']
word = ['pineapple']

choice = choice(word)


def game(word: str, attempts: int):
    secret_word = ['*'] * len(word)
    win_word = ''.join(secret_word)
    print(f'Загадано слово: {win_word}')
    while attempts > 0:
        guess_letter = input('Введіть букву або слово: ')
        if len(guess_letter) > 1:
            if guess_letter == word:
                print('Вгадали')
                break
            else:
                print('Неправильно')
        elif guess_letter in word:
            for index, letter in enumerate(word):
                if guess_letter == letter:
                    secret_word[index] = letter
                    win_word = ''.join(secret_word)
            print(win_word)
            if '*' not in secret_word:
                print('Вгадали')
                break
        elif guess_letter not in word:
            print('Цієї літери нема')
        attempts -= 1

attempts = int(input('Скільки буде спроб: '))
game(choice, attempts)





