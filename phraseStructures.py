import random
import dictionary

def greeting():
    string = [
    f"{dictionary.goodWord1()} {dictionary.TOD()} to {dictionary.count()} of my {dictionary.people1()}{punc.std()}"
    ]
    return random.choice(string)
