import random
import phraseStructures

def init():
    string = [f"{phraseStructures.greeting()}"
    ]
    return random.choice(string)
