# This is a library of helper functions.
import random
import string

def createHash():
    newHash = ""
    for i in range(0,24):
        bitF = random.randint(0,1)
        randN = random.randint(0,9)
        randL = random.choice(string.ascii_letters)
        if bitF == 0:
            newHash = newHash + f'{randL}'
        newHash = newHash + f'{randN}'
    print(newHash)
    return newHash
