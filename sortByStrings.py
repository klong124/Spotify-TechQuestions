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
