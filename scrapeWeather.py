from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import evalWeather
import evalWeatherTemp
import functions

#initialize grab for weather data
def init_grab(url):
    urlClient = urlopen(url)
    page_html = urlClient.read()
    urlClient.close()

    pageData = BeautifulSoup(page_html, "html.parser")
    dataContainer = pageData.findAll("div", {"class":"today_nowcard-section today_nowcard-condition"})

    for dataWeather in dataContainer:
        #grabs actual temp data
        tempContainer = dataWeather.findAll("div", {"class":"today_nowcard-temp"})
        temp = tempContainer[0].text
        #grabs 'feels like' temp
        feelsContainer = dataWeather.findAll("div", {"class":"today_nowcard-feels"})
        tempFeels = feelsContainer[0].text
        tempFeels2 = functions.trim_toDegree(tempFeels)
        #grabs weather condition (sunny, cloudy, ect)
        condContainer = dataWeather.findAll("div", {"class":"today_nowcard-phrase"})
        weatherCondition = condContainer[0].text
        #Debug for weather condition
		# print("WC")
		# print(weatherCondition)

	#functions to convert to int values
    intTemp = functions.trimToInt(temp)
    intFeelsTemp = functions.trimToInt(tempFeels2)
    intWeatherType = evalWeather.weatherConditionToInt(weatherCondition)
    phraseOut = evalWeatherTemp.phrase_start(intTemp, intFeelsTemp, intWeatherType)
    return phraseOut
