word = 'wordle'
length = (len(word))
remaining = 6
while remaining > 0:
    print('One word, ' + str(length) + ' letters')
    print('Guess a letter')
    letterList = word[0:length]
    guess = input()
    if guess in letterList:
        result = 1
    else:
        result = 0
    print(result)
    if result == 1:
        print('Congratulations! You guessed correctly. Your score is now ' + str(result))
    else:
        remaining = remaining - 1
        print('WRONG. You have ' + str(remaining) + ' tries remaining')

