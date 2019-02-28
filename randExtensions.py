import random
import punct

#freq1 => low frequency of occurence
def laughFreq1():
    #add space before because it is not separated in phrase structure
    string = [f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f" ahaa",
    f" ahaha yeaaa",
    f" aahah",
    f" ahaha",
    f" haha",
    f" ha",
    f" hahahaha",
    f" hahayeaa",
    f" HAHAAHA",
    f" AHAHAHAHA",
    f" HAHA",
    f" haaaaa",
    f" MUAHAHA"
    ]
    return random.choice(string)

def heyFreq1():
    string = [f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"hey{punct.std()} ",f"hey{punct.std()} ",f"hey{punct.std()} ",
    f"heyy{punct.std()} ",f"heyy{punct.std()} ",f"heyy{punct.std()} ",
    f"hay{punct.std()} ",f"hay{punct.std()} ",f"hay{punct.std()} ",
    f"aye{punct.std()} ",
    f"ayeeee{punct.std()} ",
    f"ay{punct.std()} ",
    f"ay mon{punct.std()} ",
    f"howdy{punct.std()} "
    ]
    return random.choice(string)

def emoticonFreq1():
    string = [f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",f"",
    f":)",
    f":3",
    f":-3",
    f":^)",
    f";0",
    f":-333",
    f"B^)",
    f"<(^-^)>",
    f"<>_<>",
    f"(.)_(.)",
    f"^-^"
    ]
    return random.choice(string)

#word switch
def oneWS():
    string = [f"one",f"1"]
    return random.choice(string)

def twoWS():
    string = [f"two", f"2"]
    return random.choice(string)

def withW():
    string = [f"with", f"with", f"with", f"w", f"w/", f"wit", f"wif"]
    return random.choice(string)

def plc():
    string = [f"bank", f"store", f"park", f"fair", f"beach", f"playgrounf", f"grociery store"]
    return random.choice(string)

def doSomething():
    string = [f"hang out", f"hang out {withW()} me", f"hand out", f"go to the {plc()}",
    f"goto the {plc()}", f"go to the {plc()} {withW()} me", f"go crociery shoping",
    f"go to the {plc()}", f"go to the {plc()} {withW()} me"
    ]
    return random.choice(string)
