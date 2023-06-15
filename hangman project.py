import random

if __name__ == '__main__':

    with open("listofwords.txt") as file:
        list_of_all_words = file.read().split('\n')[:-1]
        WORD = random.choice(list_of_all_words).lower()

    guess_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']

    flag = 0
    CHANCES = 3


    player_name = input("Hey, Enter your name: ")

    while not flag:
        for letter in WORD:
            if letter in guess_list or letter in vowels:
                if letter in vowels:
                    guess_list.append(letter)

                print(letter, end=' ')
            else:
                print('_', end=' ')

        print(f"\nYou have {CHANCES} chances left.")

        guess = input('Enter your guess letter: ').lower()
        guess_list.append(guess)

        if guess not in WORD:
            CHANCES -= 1

            if not CHANCES:
                break        


        flag = 1
        for letter in WORD:
            if letter not in guess_list:
                flag = 0



if flag:
    print(f"\n\t\t :::Hurray {player_name}! You got it right!::: ")
else:
    print(f"\n\t\t :::HANG MAN!! {player_name} :(::: ")
    print("\n\t\tCorrect Word:", WORD)
    
