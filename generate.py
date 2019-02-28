import random
import phraseStructures as tweetStructure

def init():
    string = [
    f"{tweetStructure.greeting()}",
    f"{tweetStructure.misc1()}",
    f"{tweetStructure.weatherPhrase()}",
    f"{tweetStructure.nwConcert()}"
    ]
    return random.choice(string)
