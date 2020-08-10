import tweepy
import pandas as pd
import time

# Personal credentials given when creating a developer account for twitter
consumerKey = " "
consumerSecret = " "
accessToken = " "
accessTokenSecret = ""

auth = tweepy.0AuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit = True)

results = []

account = "lplenglish"
numberOfTweets = 20

def tweetIt(account, numberOfTweets):
    for tweet in api.user_timeline(id = account, count = numberOfTweets):

        results.append((tweet.created_at, tweet.id,tweet.text))

        df = pd.DataFrame(results,columns = ['Date', 'Tweet_Id', 'Result'])

        df.to_csv('resultsOfLPL.csv')


tweetIt(account, numberOfTweets)