import tweepy
import pandas as pd
import time
import csv

# Personal credentials given when creating a developer account for twitter
consumerKey = "AFedVb3siHzg6ya1St27qf1fw"
consumerSecret = "EAWblXGEydwzoj1eCM6eyDBQJ0TTcBvnMzMpj4jNHtZAls2OQ2"
accessToken = "1293222169007263746-FxhpmPEnvPbjiq3YCdEYXmsX88DPr3"
accessTokenSecret = "ak8UZKIF8XcNd77DOip3W42lJ2zkvzHuniZV6gyOx5YuG"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit = True)

csvFile = open('result.csv', 'a')
account = "lplenglish"
numberOfTweets = 20
csvWriter = csv.writer(csvFile)


def tweetIt(account, numberOfTweets):
    for tweet in api.user_timeline(id = account, count = numberOfTweets):

       csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

       print(tweet.created_at, tweet.text)

        
tweetIt(account, numberOfTweets)
csvFile.close()
