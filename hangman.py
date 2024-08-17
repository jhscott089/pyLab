word = 'wordle'
guess =

# wordState function will create show the letters that have been guessed in the order in which they belong
def wordState():
    blank = '______'
def game():
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
        if len(guess) > 1:
            print('Input invalid: May only guess single letter.')
            break
        guessList += guess

        if guess in letterList:
            result = 1
        else:
            result = 0
        if result == 1:
            cGuessCount = cGuessCount + 1
            if cGuessCount == length:
                print('Congratulations, you won! Play again? Type "Y" or "N"')
                input()
            else:
                guessIndex = letterList.index(guess)
                print(placementVar.index[guessIndex])
                print('Correct! You have correctly guessed ' + str(cGuessCount) + ' letters so far')
        else:
            remaining = remaining - 1
            if remaining == 0:
                print('You have died.')
                break
            else:
                print('WRONG. You have ' + str(remaining) + ' tries remaining.')


game()