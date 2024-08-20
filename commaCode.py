def commaCode(list1):
    lLength= len(list1)
    lString = ''
    for i in list1[0:lLength - 1]:
        lString += i + ', '
    lString += "and " + list1[lLength - 1] + "."
    print(lString)



spam = []
commaCode(spam)