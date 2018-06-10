def sortByStrings(s, t):
    result = []
    for c in t:
        for i in range(s.count(c)):
            result += c
            
    return ''.join(result)
    
    
print sortByStrings('weather', 'therapyw')
print sortByStrings('good', 'odg')
print sortByStrings('odg', 'god')
print sortByStrings('tomorrow', 'wot')
print sortByStrings('tomorrow', 'wat')
print sortByStrings('tomorrow', 'what')
print sortByStrings('', '')
print sortByStrings('d', '')
print sortByStrings('', 'e')
print sortByStrings('dog', 'cat')
print sortByStrings('dog', 'dog')
print sortByStrings('dog', 'dogzilla')
print sortByStrings('dogzilla', 'dog')









#the following code assumes that input will be given correctly
##for example, that brackets will never be given without a number preceding

import re

def decodeString(s):
    result = ''
    arr = s.split(']')
    for el in arr:
        newarr = list(reversed(el.split('[')))
        for index, ting in enumerate(newarr): #ting is a technical term
            string = ''
            letters = re.match('[a-zA-Z]+', ting)
            if letters:
                string = letters.group()
                
            number = re.search('[0-9]+', ting)
            if number:
                for i in range(int(number.group())):
                    string += newarr[index - 1]
                    newarr[index] = string
        result += newarr[-1]
    return result
    
    
print decodeString('4[ab]')
print decodeString('2[b3[a]]')
print decodeString('2[b]2[a]')
print decodeString('b2[a]')
print decodeString('b[a]') # this does not give correct output as it is not encoded correctly









def changePossibilities(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0 or len(denominations) <= 0 or denominations[0] == 0:
        return 0
    return changePossibilities(amount - denominations[0], denominations) + changePossibilities(amount, denominations[1:])
    
print changePossibilities(4, [1, 2, 3])
print changePossibilities(5, [1, 2, 3])
print changePossibilities(1, [1, 2, 3])
print changePossibilities(3, [1, 2, 3])
print changePossibilities(0, [1, 2, 3]) # unclear whether this case should return 1 or 0, but here it returns 1
print changePossibilities(-1, [1, 2, 3])
print changePossibilities(9, [1, 7, 9])
print changePossibilities(10, [10])
print changePossibilities(4, [10, 1])
print changePossibilities(10, [10, 1])
print changePossibilities(10, [0])
print changePossibilities(10, [])
print changePossibilities(10, [0, 1, 2, 3, 4]) # as 0 should not be a denomination (makes no sense), this will return 0
