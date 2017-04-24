upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
num = '1234567890'
sym = '.?!&#,;:-_*'


def check(password):
    up = False
    low = False
    n = False
    for x in password:
        if x in upper:
            up = True
        elif x in lower:
            low = True
        elif x in num:
            n = True
    return up and low and n

def strength(password):
    up = False
    low = False
    n = False
    s = False
    r = 0
    l = len(password)
    if(l<3):
        return 1
    elif (l>8):
        r+=2
    elif (l>5):
        r+=1
    for x in password:
        if x in upper:
            up = True
        elif x in lower:
            low = True
        elif x in num:
            n = True
        elif x in sym:
            s = True
    if(up):
        r+=2
    if(low):
        r+=2
    if(n):
        r+=2
    if(s):
        r+=2
    return r


"""
print check('a') # F
print check('abC') # F
print check('ABC') # F
print check('ABC1') # F
print check('abc123') # F
print check('aBc123') # T
print check('0Hr') # T
print check('ohN0') # T

print strength('a') 
print strength('aBBBB') 
print strength('acaatt2') 
print strength('a???R13')
print strength('a!lka48905DL') 
print strength('87652345678')
"""
