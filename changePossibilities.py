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
