#Program to find out how often a streak of six heads or six tails comes up in a randomly generated list of heads and tails.
#
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip = []
    flip = random.randint(0, 1)
    print(len(flip))


    # Code that checks if there is a streak of 6 heads or tails in a row.
for i in list:
    if i[-3:3] == 0:
        count = 1
    elif i[-3:3] == 6:
        count = 1
#print('Chance of streak: %s%%' % (numberOfStreaks / 100))