import math
import random

#probability of tweeting a picture
def genImg():
    if random.randint(0,10) > 5:
        return True
    else:
        return False

def selectImg():
    string = [
    'img/grape.png',
    'img/cat_meme1.jpg',
    'img/egg.jpg'
    ]
    return random.choice(string)

def genNumber():
    textNumber = str(convertNum(random.randint(0, 99)))
    #print(type(textNumber))
    textNumber = textNumber + getTextNumberL()
    return textNumber

def getTextNumberL():
    string = [f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"hundred",
    f"hundred",
    f"thousand",
    f"billion trillion million",
    f"gazillion",
    f"undecillion",
    f"hundo",
    f"one-hundredths"
    ]
    return random.choice(string)

def convertNum(randomInt):
    if(randomInt < 20):
        return switchNum
    elif (randomInt >= 20):
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

def switchNum(Integer):
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
    return case.get(Integer)

#return either word or number
#ex: "9 + 10" or "nine plus ten"
def useNumOrWord(Integer):
    string = [str(Integer),
    switchNum(Integer)
    ]
    return random.choice(string)

#removes degree sign and converts to int
def trimToInt(temps):
	x = len(temps)
	#y = x-1
	int_temps = int(temps[:x-1])
	return int_temps

#trims feels like string down to degree sign
def trim_toDegree(string):
	if not string:
		return ""

	ignoreChar = ' '
	x = 0
	while x < len(string) and string[x] == ignoreChar:
		x = x+1
	y = len(string )-1
	while y>=0 and string[y] == ignoreChar:
		y = y-1

	lengthBuffer = len("Feels Like")
	return string[x+lengthBuffer+1:y+1]
