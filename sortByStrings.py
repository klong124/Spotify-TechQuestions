def sortByStrings(s, t):
    result = []
    for c in t:
        for i in range(s.count(c)):
            result += c
            
return ''.join(result)
