#sk condition to int value
def weatherConditionToInt(conditionString):
	#evaluate weather condition

	#for weatherConditionValueL
	#value "0" = clear weather, nice, enjoyable
	#value "1" = cloudy weather, so - so weather
	#value "2" = light rain, ect
	#value "3" = heavy rain, stormy, ect

	weatherConditionValue = 0
	if conditionString == "Cloudy":
		weatherConditionValue = 1
	if conditionString == "Partly Cloudy":
		weatherConditionValue = 1
	if conditionString == "Mostly Cloudy":
		weatherConditionValue = 1
	if conditionString == "Fair":
		weatherConditionValue = 1
	if conditionString == "Light Rain":
		weatherConditionValue = 2
	if conditionString == "Rainy":
		weatherConditionValue = 3
	return weatherConditionValue
