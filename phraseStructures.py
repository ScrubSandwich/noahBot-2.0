import random
import dictionary
import punct
import randExtensions
import scrapeWeather

def greeting():
    string = [
    f"{dictionary.goodWord1()} {dictionary.TOD()} to {dictionary.count()} of my {dictionary.people1()}{randExtensions.laughFreq1()}{punct.std()} {randExtensions.emoticonFreq1()}",
    f"A {dictionary.goodWord2()} to {dictionary.count()} of my {dictionary.people1()}{randExtensions.laughFreq1()}{punct.std()} {randExtensions.emoticonFreq1()}",
    f"{dictionary.wish1()} {dictionary.count()} of my {dictionary.people1()} {dictionary.verbBe1()} {dictionary.verbHaving1()} a {dictionary.goodWord2()} {dictionary.TOD()}{randExtensions.laughFreq1()}{punct.std()} {randExtensions.emoticonFreq1()}"
    ]
    return random.choice(string)

def misc1():
    string = [
    f"{randExtensions.heyFreq1()}wats nine plus ten{randExtensions.laughFreq1()}{punct.stdFreq1()} {randExtensions.emoticonFreq1()}",
    f"does any {randExtensions.oneWS()} want {randExtensions.twoWS()} {randExtensions.hangWS()} out{randExtensions.laughFreq1()}{punct.stdFreq1()} {randExtensions.emoticonFreq1()}"
    f"{links.nw()}"
    f"{randExtensions.heyFreq1()}"
    ]
    return random.choice(string)

def weatherPhrase():
    url = 'https://weather.com/weather/today/l/46304:4:US'
    scrapeWeather.init_grab(url)
