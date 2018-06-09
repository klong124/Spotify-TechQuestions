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
