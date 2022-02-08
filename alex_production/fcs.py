from os import getenv
from dotenv import load_dotenv
import tweepy

load_dotenv(r"C:\Users\Alex Lucchesi\OneDrive\Documents\GitHub\congressional_sentiment_NLP\alex_production\.env")
ak = getenv("API_KEY")
aks = getenv("API_KEY_SECRET")
at = getenv("ACCESS_TOKEN")
ats = getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(ak, aks)
auth.set_access_token(at, ats)
api = tweepy.API(auth)

def get_tweets(username):
    tweets = api.user_timeline(screen_name = username)
    for tweet in tweets:
        print(tweet.text)

    
