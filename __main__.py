import random
import sched, time
import datetime
from time import gmtime, strftime, sleep
import tweepy
import math
import generate
import functions

print("---running noahBot_2.0---")

schedule = sched.scheduler(time.time, time.sleep)

# j is time in seconds
# 900s == 15 mins
j = 15
sec = j

def phrase_start():
    tweetOut = "Null"
    tweetOut = generate.init()
    return tweetOut

def main(sc):
    sec = j
    phrase_final = phrase_start()
    argfile = "twitterlog.txt"

    #defines twitter authentication keys and tweepy API
    cachedTweet = open(argfile, 'w')
    cachedTweet.write(phrase_final)
    cachedTweet.close()

    consumer_key = 'XvlJXaQ6ovTo1gOqh9WVMeU7M'
    consumer_secret  = 'xg0ckn4YNDF5bPdATQ7Bf9pRZgE0MPoikQoGkndy6LC3H0NszO'
    access_key = '505149026-oStxD37BQClezeljensQc0rZLcXBykLvc4PUX7TD'
    access_secret = 'tVYMzZUmGF0atPW4rfLpqT2EgMgL6EpqQG7T2QXuBZsjC'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    cachedTweet = open(argfile, 'r')
    f = cachedTweet.readlines()
    cachedTweet.close()

    #capture tweet time
    datetimeStr = str(datetime.datetime.now())

    for line in f:
        try:
            genImgBool = functions.genImg()
            if genImgBool == False:
                api.update_status(line)
                print("\"" + line + "\" tweeted at " + datetimeStr)
            elif genImgBool == True:
                print("load img")
                api.update_with_media(f'{functions.selectImg()}', status="Haha Look At This Funny Picture!")
                print("image tweeted at " + datetimeStr)
            else:
                print("functions.genImg() != True or False... Could there be a logic error somewhere?")
                api.update_status("functions.genImg() != True or False... Could there be a logic error somewhere?")
        except tweepy.error.TweepError:
            print("Error: tweet not posted...")
            print("Was there a duplicate tweet?")
    schedule.enter(sec,1,main,(sc,))
schedule.enter(sec,1,main,(schedule,))
schedule.run()
