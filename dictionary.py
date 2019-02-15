import random
import functions
import evalTime

def noun1():
    string = [f"",
    ]
    return random.choice(string)

def verbBe1():
    string = [f"are",
    f"will be",
    f"are goinf to be",
    f"are going to be",
    f"are gonna be",
    f"r gunna b",
    f"will b",
    f"will soon be",
    f"finna be"
    ]
    return random.choice(string)

def verbHaving1():
    string: = [f"having",

    ]

def adj1():
    string = [f"",
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
    f"grand",
    f"next level",
    f"greaaat",
    f"great",
    f"fabulous",
    f"spiritual",
    f"epic",
    f"EPICCC",
    f"legendary",
    f"nice/cool",
    f"cool",
    f"nice",
    f"very nice"
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
    f"like, {functions.genNumber()}-percent",
    f"like, half",
    f"allll",
    f"allllllll",
    f"many",
    f"a lot",
    f"over nine thousand",
    f"twenny one",
    f"21",
    f"sixty-nine",
    f"a whole bunch",
    f"a wholleeee bunch",
    f"every single one",
    f"each and every one",
    f"every one"
    ]
    return random.choice(string)

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
    f"sisters",
    f"brothers and sisters",
    f"family members",
    f"commune members",
    f"twitter users",
    f"Twitter users",
    f"corporate slaves",
    f"people",
    f"mfs",
    f"fellow humans",
    f"fellow homo sapiens",
    f"fellow mortals",
    f"mortal friends",
    f"pplz",
    f"fwendz"
    ]
    return random.choice(string)

def wish1:
    string = [f"I'm wishing",
    f"I hope",
    f"I hope that",
    f"In the forseeable future, I envision",
    f"According to my research,",
    f"According to my magic 8 ball,",
    f"I envision",
    f"I will see to it that"
    ]
    return random.choice(string)

#-----------------#
#weather dictionary:

def shockWord1():
	string = [f"WOW",
    f"Wow",
    f"Wooowwwwww",
    f"WOWWWW",
    f"Woahhhhh",
	f"WOAHHH",
    f"DANGGGG",
    f"Dang",
    f"Holy smokes",
    f"Brooooo",
    f"Duuudeeeee",
    f"What the",
	f"Danngggg",
    f"*Is panting from the heat*",
    f"*While dying of heat stroke*",
    f"*Wipes sweat from face*"
    ]
	return random.choice(string)

#gen word for "today" - used with hot temps
def todayW1():
	DN = evalTime.timeDN(evalTime.getHour())
	string = [f"to{DN}",
    f"outside",
    f"outside to{DN}",
    f"out",
    f"out here",
    f"out here to{DN}"
    ]
	return random.choice(string)

#gens a term for nice
#used to begin a sentence, starts with capital
def niceWord():
	string = [f"Epic",
    f"Nice",
    f"Sweet",
    f"Cool",
    f"Not bad",
    f"Dopeeeee",
    f"Pretty cool"
    ]
	return random.choice(string)

#gens a term for nice
#used to replace the word nice, does not have caps
def niceWordNC():
	string = [f"epic",
    f"nice",
    f"sweet",
    f"fresh",
    f"sweet",
    f"comfortable",
    f"relaxing"
    ]
	return random.choice(string)

#selects a term for "now"
#ends with the term "is"
def nowTerm():
	DN = evalTime.timeDN(evalTime.getHour())
	string = [f"right now is",
    f"right now is",
    f"right now is",
    f"is currently",
    f"is",
    f"to{DN} is"
    ]
	return random.choice(string)

#selects a term for "now"
#does not end with the term "is"
def nowTermNIS():
	string = [f"right now",
    f"right now",
    f"right now",
    f"rn"
    ]
	return random.choice(string)

#word choice temp or temperature
def tempW():
	string = [f"temp", f"temperature"]
	return random.choice(string)

#syn for hot
def hotSyn():
	string = [f"hot",f"steamy",f"warm"]
	return random.choice(string)

#picks a 'swear' word
def swearW1():
	string = [f"heck",f"h*ck",f"eff"]
	return random.choice(string)
