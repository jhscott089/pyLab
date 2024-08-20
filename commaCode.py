# A function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.

def commaCode(list1):
    lLength= len(list1)
    lString = ''
    for i in list1[0:lLength - 1]:
        lString += i + ', '
    lString += "and " + list1[-1] + "."
    return(lString)

spam = ["a","b"]
print(commaCode(spam))