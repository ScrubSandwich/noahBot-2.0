import phraseStructures_Weather as pSW

#categorizes temp by number value then passes to another function to generate a phrase
def phrase_start(temp, feelsTemp, weatherType):
    #debug
    # print("weatherType: ")
	# print(weatherType)
	phraseOut = "NO TEMP DATA"
	if weatherType == 0:
		if temp >= 60:
			if temp < 80:
				phraseOut = pSW.temp60to79(temp)
		elif temp >= 80:
			if temp < 90:
				phraseOut = pSW.temp80to89(temp)
		elif temp >= 90:
			phraseOut = pSW.temp90plus(temp)

	if weatherType == 1:
		if temp < 1:
			phraseOut = "BELOW_1F"
		elif temp >= 1:
			if temp < 21:
				phraseOut = "GREATER_1F, BELOW_21F"
		elif temp == 21:
			phraseOut = "WEATHER_IS_21F"
		elif temp >= 22:
			if temp < 30:
				phraseOut = "GREATER_22F, BELOW_30F"
		elif temp >= 30:
			if temp < 40:
				phraseOut = "GREATER_30F, BELOW_40F"
		elif temp >= 60:
			if temp < 80:
				phraseOut = pSW.temp60to79_WC1(temp)
		elif temp >= 80:
			if temp < 90:
				phraseOut = pSW.temp80to89_WC1(temp)
		elif temp >= 90:
			phraseOut = pSW.temp90plus_WC1(temp)
	return phraseOut
