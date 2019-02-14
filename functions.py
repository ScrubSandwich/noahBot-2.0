from random import *
from math import floor

def genNumber():
    textNumber = convertNum(randint(0, 99))
    textNumber += [f"hundred",
    f"hundred",
    f"thousand",
    f"",
    f"",
    f"",
    f""
    ]
    return textNumber

def convertNum(randomInt):
    if(randomInt < 20):
        return switchNum
    else:
        if(randomInt%10 == 2):
            suffix = switchNum(math.floor(randomInt/10))
            return "twenty-" + suffix
        if(randomInt%10 == 3):
            suffix = switchNum(math.floor(randomInt/10))
            return "thirty-" + suffix
        if(randomInt%10 == 4):
            suffix = switchNum(math.floor(randomInt/10))
            return "fourty-" + suffix
        if(randomInt%10 == 5):
            suffix = switchNum(math.floor(randomInt/10))
            return "fifty-" + suffix
        if(randomInt%10 == 6):
            suffix = switchNum(math.floor(randomInt/10))
            return "sixty-" + suffix
        if(randomInt%10 == 7):
            suffix = switchNum(math.floor(randomInt/10))
            return "seventy-" + suffix
        if(randomInt%10 == 8):
            suffix = switchNum(math.floor(randomInt/10))
            return "eighty-" + suffix
        if(randomInt%10 == 9):
            suffix = switchNum(math.floor(randomInt/10))
            return "ninety-" + suffix

def switchNum(randomInt):
    case = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    return case.get(randomInt)
