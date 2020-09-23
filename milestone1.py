import tweepy
import webbrowser
import time
import flask 
import os
import random
from dotenv import load_dotenv
from os.path import join 
from tweepy import OAuthHandler
from tweepy import Cursor
from datetime import datetime, date, time, timedelta


"""
dotenv_path = join(dirname(__file__), 'Twitter.env')
load_dotenv(dotenv_path)
"""

twitterConsumerKey = os.environ["TWITTER_CONSUMER_KEY"]
twitterConsumerSecret = os.environ["TWITTER_CONSUMER_SECRET"]

accessToken = os.environ["ACCESS_TOKEN"]
accessTokenSecret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(twitterConsumerKey,twitterConsumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)

flag = True

"""

foodList = ['French Toast','Poutine','Chicken Nuggets','Veggie Burger','Sushi','Tacos','Dosa','Pho','Chicken Kebab','Pizza','Lobster']
chosenOne = random.choice(foodList)

search = api.search(chosenOne)
length = len(search) - 2
    
randomNumber = random.randint(0,length)


text = search[randomNumber].text
date = search[randomNumber].created_at
screenName = search[randomNumber].user.screen_name
name = search[randomNumber].user.name
url = search[randomNumber].user.url

"""

""""
print(text) 
print(date)
print(screenName)
print(name)
print(url)

"""

app = flask.Flask(__name__)
 
@app.route('/')
 
def index():
    
    foodList = ['French Toast','Poutine','Chicken Nuggets','Veggie Burger','Sushi','Tacos','Dosa','Pho','Chicken Kebab','Pizza','Lobster']
    chosenOne = random.choice(foodList)

    search = api.search(chosenOne)
    length = len(search) - 2
    
    randomNumber = random.randint(0,length)


    text = search[randomNumber].text
    date = search[randomNumber].created_at
    screenName = search[randomNumber].user.screen_name
    name = search[randomNumber].user.name
    url = search[randomNumber].user.url
    

    
    return flask.render_template(
        
        "index.html",
        chosenOne = chosenOne,
        text = text,
        date = date,
        screenName = screenName,
        name = name,
        url = url
        
        
        )
    
app.run(
    
    port=int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0')
    
    )
    
    


 
"""
     
    myList = ["Khalid","BlackBear","Drake","AZ","Selena Gomez"]
    lengthOfMyList = len(myList)
     
    return flask.render_template(
         
        "index.html",
        artists = myList,
        listLength = lengthOfMyList
         
         
        )
        
"""