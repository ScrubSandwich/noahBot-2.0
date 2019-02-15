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

def emoticonFreq1:
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
def oneWS:
    string = [f"one",f"1"]
    return random.choice(string)

def twoWS:
    string = [f"two", f"2"]
    return random.choice(string)

def hangWS:
    string = [f"hang", f"hang", f"hang", f"hang", f"hand"]
    return random.choice(string)
