import random

print('H A N G M A N')
word = ['python', 'java', 'kotlin', 'javascript']
winner_word_random = random.choice(word)
winner_word_random_len = len(winner_word_random)
rest = winner_word_random_len - 3
winner_word = winner_word_random[0:3]
guess = input('Guess the word ' + winner_word + '-'*rest)
if guess == winner_word_random.lower():
    print('You survived!')
else:
    print('You lost!')