def waterState(f):
    if f <= 32:
        return "solid"
    elif f >= 212:
        return "gas"
    else:
        return "liquid"

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

def toGerman(word):
    if word == "yes":
        return "ja"
    elif word == "no":
        return "nein"

def stopLight(c):
    if c == "red":
        return "stop"
    elif c == "green":
        return "go"
    else:
        return "slow"

