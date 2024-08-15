word = 'wordle'
length = (len(word))
remaining = int(length)
import sys
cGuessCount = 0
guessList = []
while remaining > 0:
    print('One word, ' + str(length) + ' letters')
    print('Guess a letter')
    pl = str(guessList)
    if pl != '[]':
        print('Guesses so far: ' + pl)
    letterList = word[0:length]
    guess = input()
    guessList += guess

    if guess in letterList:
        result = 1
    else:
        result = 0
    if result == 1:
        cGuessCount = cGuessCount + 1
        print('Congratulations! You guessed correctly. Your score is now ' + str(cGuessCount))
    else:
        remaining = remaining - 1
        if remaining == 0:
            print('You have died.')
            break
        else:
            print('WRONG. You have ' + str(remaining) + ' tries remaining.')


