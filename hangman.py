word = 'wordle'

# wordState function will create show the letters that have been guessed in the order in which they belong
def game():
    length = (len(word))
    remaining = int(length)
    import sys
    import copy
    cGuessCount = 0
    guessStatus = ['#' * len(word)]  ## This needs to be modified to create a separate entry for each letter rather than single string
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
                guessIndex = word.index(guess)
                guessStatus[guessIndex] = guess

                print('Correct!' + guessStatus) #Show the word with hashes to fill in unguessed letters
        else:
            remaining = remaining - 1
            if remaining == 0:
                print('You have died.')
                break
            else:
                print('WRONG. You have ' + str(remaining) + ' tries remaining.')


game()