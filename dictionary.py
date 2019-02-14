import random
import functions

def noun1():
    string = [f"",
    ]
    return random.choice(string)

def verb1():
    string = [f"",
    ]
    return random.choice(string)

def adj1():
    string = [f"",
    ]
    return random.choice(string)

def welcome():
    string = [f"Hello",
    f"{goodWord1()} {TOD()} to {count()}",
    f"A {goodWord2()} {TOD()} to {count()}",
    f"Hello",
    ]
    return random.choice(string)

def goodWord1():
    string = [f"Good",
    f"Goooooood",
    f"Goooooooooooooooood",
    f"Hello and good"
    f"good",
    f"hood",
    f"goof"
    ]
    return random.choice(string)

def goodWord2():
    string = [f"good",
    f"fantastic",
    f"lovely",
    f"grand"
    ]
    return random.choice(string)

def TOD():
    string = [f"morning",
    f"evening",
    f"morrow",
    f"night time",
    f"sleepy time",
    f"midnight",
    f"tea-time",
    f"lunch break",
    f"lunch-time",
    f"mornin'",
    f"mid- to late-evening",
    f"early morning",
    f"noon-time",
    f"afternoon"
    ]
    return random.choice(string)

def count():
    string = [f"all",
    f"some",
    f"most",
    f"a good chunk",
    f"{functions.genNumber()}-percent",
    f""
    ]

def people1():
    string = [f"friends",
    f"followers",
    f"royal subjects",
    f"pals",
    f"peasants",
    f"citizens",
    f"hoodlums",
    f"buddies",
    f"friennz",
    f"frenz",
    f"brothers",
    f"sisters"
    f"brothers and sisters",
    f"family members",
    f"commune members",
    f"twitter users",
    f"Twitter users",
    f"corporate slaves",
    f"people"
    ]
