from random import choice

word = ['apple', 'orange', 'pineapple', 'watermelon', 'melon', 'grape']

choice = choice(word)

def game(word: str):
    attempts = int(input('Скільки буде спроб: '))
    count_attempts = attempts - 1
    while True:
        guess_letter = input('Введіть букву або слово: ')
        if count_attempts == 0:
            print('Програли')
            break
        if len(guess_letter) > 1:
            if guess_letter == word:
                print('Вгадали')
                break
            else:
                print('Неправильно')
                count_attempts -= 1


game(choice)





