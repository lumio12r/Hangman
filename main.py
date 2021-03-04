import random
import string

print('H A N G M A N\n')

random_word = random.choice(['python', 'java', 'kotlin', 'javascript'])
guessed_word = "-" * len(random_word)
letters = [i for i in string.ascii_lowercase]
all_letters_use = []
print(guessed_word)
count = 0

while count < 9:
    guess = input('Input a letter: ')

    if len(guess) > 1:
        print("You should input a single letter")
        if count == 8:
            print('You lost!')
            break
    elif (guess not in letters) or (guess == guess.upper()):
        print("Please enter a lowercase English letter")
        if count == 8:
            print('You lost!')
            break
    elif (guess in all_letters_use) or (guess in guessed_word):
        print("You've already guessed this letter")
        if count == 8:
            print('You lost!')
            break
    elif guess not in random_word:
        print("That letter doesn't appear in the word")
        all_letters_use.append(guess)
        count += 1
        if count == 8:
            print('You lost!')
            break
    elif guess in guessed_word:
        print("No improvements")
        if count == 8:
            print('You lost!')
            break
    else:
        for i in range(0, len(random_word)):
            if random_word[i] == guess:
                guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
                if guessed_word == random_word:
                    print('You guessed the word!\nYou survived!')
                    exit()
    print(f'\n{guessed_word}')


