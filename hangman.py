word = 'wordle'
length = (len(word))
remaining = int(length)
import sys
guessList = 0
while remaining > 0:
    print('One word, ' + str(length) + ' letters')
    print('Guess a letter')
    letterList = word[0:length]
    guess = input()

    if guess in letterList:
        result = 1
    else:
        result = 0
    if result == 1:
        guessList = guessList + 1
        print('Congratulations! You guessed correctly. Your score is now ' + str(guessList))
    else:
        remaining = remaining - 1
        if remaining == 0:
            print('You have died.')
            break
        else:
            print('WRONG. You have ' + str(remaining) + ' tries remaining. Letters guessed so far:' + str(guessList))


