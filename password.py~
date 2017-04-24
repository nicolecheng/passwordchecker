UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
NUMS = '0123456789'
SYMBOLS = '.?!&#,;:-_*'
MIN_LEN = 7


def minimum(password):
    a = [True for x in password if x in UPPER]
    b = [True for x in password if x in LOWER]
    c = [True for x in password if x in NUMS]
    return True in a and True in b and True in c


print minimum('asdf')
print minimum('ASDF')
print minimum('ASdf')
print minimum('ASdf1')
print minimum('asdiFjasig1234j')


def strength(password):
    ret = 0
    criteria = [[True for x in password if x in UPPER],
                [True for x in password if x in LOWER],
                [True for x in password if x in NUMS],
                [True for x in password if x in SYMBOLS],
                [len(password) > MIN_LEN]]
    for x in criteria:
        if True in x:
            ret += 2
    return ret


print strength('asdf')
print strength('Asdf')
print strength('Asdf1')
print strength('Asdf1!')
print strength('AsDfGhJkL123!@#')
