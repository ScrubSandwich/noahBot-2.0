import random
import dictionary
import punct
import evalTime

#generates phrase for 90+  for weather Condition 0
#WC0
def temp90plus(temp):
	string = [f"{dictionary.shockWord1()}{punct.std()} It's {temp}\u00b0{dictionary.todayW1()}{punct.std()}"]
	return random.choice(string)

#generates phrase for temps between 80 and 89 for weather Condition 0
#WC0
def temp80to89(temp):
	string = [f"Pretty {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Real steamer {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Pretty {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Really {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Rather {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Well{punct.std()} it's {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}"]
	return random.choice(string)

#generates phrase for temps between 60 and 79 for weather Condition 0
#WC0
def temp60to79(temp):
	if temp == 69:
		string = [f"The temp is {temp}\u00b0{punct.std()} {dictionary.niceWord()}{punct.std()}",
		f"{dictionary.niceWord()}{punct.std()} {temp}\u00b0{punct.std()}"]
	if temp != 69:
		string = [f"The {dictionary.tempW()} to{evalTime.timeDN(evalTime.getHour())} is {temp}\u00b0{punct.std()} Should be a nice {evalTime.timeDN(evalTime.getHour())} to{evalTime.timeDN(evalTime.getHour())}{punct.std()}",
		f"Hmm... Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Not too shabby{punct.std()}",
		f".........{temp}\u00b0........ Not a bad {dictionary.tempW()}{punct.std()} Go out and enjoy the {evalTime.timeDN(evalTime.getHour())}{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Can't complain{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Not bad{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Not gonna lie{punct.std()} It's a great {evalTime.timeDN(evalTime.getHour())} out{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Doesn't get any better than this{punct.std()}",
		f"It would appear the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0{punct.std()} Talk about nice weather{punct.std()}",
		f"Sure is {dictionary.niceWordNC()} {dictionary.nowTermNIS()}{punct.std()} The {dictionary.tempW()} is {temp} and there are clear skies as far as the eye can see{punct.std()}",
		f"Sure is {dictionary.niceWordNC()} {dictionary.nowTermNIS()}{punct.std()} The {dictionary.tempW()} is {temp} and there are blue skies as far as the eye can see{punct.std()}",
		f"Not gonna lie{punct.std()} It's pretty darn {dictionary.niceWordNC()} out{punct.std()} The {dictionary.tempW()} is {temp}{punct.std()}"]
	return random.choice(string)

#---WC1---

#generates phrase for cloudy weather
def phraseIsCloudy():
	cloudyPhrase = [f"with a bit of over cast",f"and cloudy",f"with cloudy skies as far as the eye can see",f"and no sign of sunshine",f"with overcast"]
	return random.choice(cloudyPhrase)

#generates phrase for 90+ for weather Condition 1
#WC1
def temp90plus_WC1(temp):
	string = [f"{dictionary.shockWord1()}{punct.std()} It's {temp}\u00b0 {dictionary.todayW1()} {phraseIsCloudy()}{punct.std()}"]
	return random.choice(string)

#generates phrase for temps between 80 and 89 for weather Condition 1
#WC1
def temp80to89_WC1(temp):
	string = [f"Pretty {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Real steamer {dictionary.todayW1()}{punct.std()} Too bad it's cloudy. The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Pretty {dictionary.hotSyn()} {dictionary.todayW1()}{punct.std()} Cloudy though... The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Really {dictionary.hotSyn()} {dictionary.todayW1()} {phraseIsCloudy()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}",
	f"Rather {dictionary.hotSyn()} {phraseIsCloudy()} {dictionary.todayW1()}{punct.std()} The {dictionary.tempW()} is {temp}\u00b0{punct.std()}"]
	return random.choice(string)

#generates phrase for temps between 60 and 79 for weather Condition 1
#WC1
def temp60to79_WC1(temp):
	if temp == 69:
		string = [f"The temp is {temp}\u00b0 {phraseIsCloudy()}{punct.std()} {dictionary.niceWord()}{punct.std()}",
		f"{dictionary.niceWord()}{punct.std()} {temp}\u00b0{phraseIsCloudy()}{punct.std()}"]
	if temp != 69:
		string = [f"The {dictionary.tempW()} to{evalTime.timeDN(evalTime.getHour())} is {temp}\u00b0 {phraseIsCloudy()}{punct.std()} Should have been a nice {evalTime.timeDN(evalTime.getHour())} to{evalTime.timeDN(evalTime.getHour())} but we don't always get what we want, now do we?",
		f"Hmm... Looks like the {dictionary.tempW()} {dictionary.nowTerm()} {temp}\u00b0 {phraseIsCloudy()}. Mehh{punct.std()}",
		f".........{temp}\u00b0........ Not a bad {dictionary.tempW()}, but its gonna be cloudy for the time being{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.niceWord()} {temp}\u00b0. Can't complain about the temp but its still cloudy {dictionary.todayW1()}{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.niceWord()} {temp}\u00b0 {phraseIsCloudy()}. Not bad but certainly not great{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.niceWord()} {temp}\u00b0 {phraseIsCloudy()}. But don't let that bring you down{punct.std()} A few clouds never hurt anyone{punct.std()}",
		f"Looks like the {dictionary.tempW()} {dictionary.niceWord()} {temp}\u00b0 {phraseIsCloudy()}. Could be worse I suppose{punct.std()}",
		f"The {dictionary.tempW()} is {temp}\u00b0 {phraseIsCloudy()}{punct.std()} What do you want me to do about it?",
		f"The {dictionary.tempW()} is {temp}\u00b0 {phraseIsCloudy()}{punct.std()} What the {dictionary.swearW1()} do you want me to do about it?"]
	return random.choice(string)
