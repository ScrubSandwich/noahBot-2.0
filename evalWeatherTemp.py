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
		if temp >= 80:
			if temp < 90:
				phraseOut = pSW.temp80to89(temp)
		if temp >= 90:
			phraseOut = pSW.temp90plus(temp)

	if weatherType == 1:
        if temp < 1:
            
        if temp >= 1:
            if temp < 21:

        if temp == 21:
            #weather is 21
        if temp >= 22:
            if temp < 30:

        if temp >= 30:
            if temp < 40:

		if temp >= 60:
			if temp < 80:
				phraseOut = pSW.temp60to79_WC1(temp)
		if temp >= 80:
			if temp < 90:
				phraseOut = pSW.temp80to89_WC1(temp)
		if temp >= 90:
			phraseOut = pSW.temp90plus_WC1(temp)
	return phraseOut
