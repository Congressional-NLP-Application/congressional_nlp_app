from os import getenv
from re import S
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import tweepy

db = "tweets.db"
load_dotenv(r"C:\Users\Alex Lucchesi\OneDrive\Documents\GitHub\congressional_sentiment_NLP\alex_production\.env")
ak = getenv("API_KEY")
aks = getenv("API_KEY_SECRET")
at = getenv("ACCESS_TOKEN")
ats = getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(ak, aks)
auth.set_access_token(at, ats)
api = tweepy.API(auth)


handles = pd.read_csv('twitter_handles.csv')
handles = handles.twitter_handle

def get_tweets():
    l = []
    for handle in handles:
        tweets = api.user_timeline(screen_name = str(handle))
        for tweet in tweets:
            l.extend([[handle, tweet.text]])
    return l
            
def create_table():
    con = sqlite3.connect(db)
    cur = con.cursor()
    print("Connection Created to Database")
    cur.execute(''' CREATE TABLE IF NOT EXISTS tweets
                  (handle, tweet_text)''')
    con.commit()
    con.close()
    print("Table successfully Created")
    
def add_tweets():
    con = sqlite3.connect(db)
    cur = con.cursor()
    print("Successful Connection to Database")
    
    t = get_tweets()
    cur.executemany("insert into tweets values (?, ?)", t)
    con.commit()
    con.close()
    print("Tweets successfully inserted into table")
    
def drop_table():
    con = sqlite3.connect(db)
    cur = con.cursor()
    print("Connection created to database")
    
    cur.execute(' DELETE FROM tweets')
    con.commit()
    con.close()
    print("Table successfully deleted")
    


