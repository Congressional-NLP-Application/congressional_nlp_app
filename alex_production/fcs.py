"""
Need to pull full tweet length instead of link for rest of tweet

"""

from os import getenv
from re import S
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import tweepy

#Set up database
db = "tweets.db"

# Load in environment variables for api access, set to local variables
load_dotenv()
ak = getenv("API_KEY")
aks = getenv("API_KEY_SECRET")
at = getenv("ACCESS_TOKEN")
ats = getenv("ACCESS_TOKEN_SECRET")

# Instantiate and set tweepy access token
auth = tweepy.OAuthHandler(ak, aks)
auth.set_access_token(at, ats)
api = tweepy.API(auth)

# read in twitter handles pulled from Git
handles = pd.read_csv('twitter_handles.csv')
handles = handles.twitter_handle

def get_tweets():
    l = []
    for handle in handles:
        tweets = api.user_timeline(screen_name = str(handle))
        for tweet in tweets:
<<<<<<< Updated upstream
            l.extend([[handle, tweet.text]])
    print("API has successfully scraped all tweets from Senators.")
    return l
            
def create_table():
    con = sqlite3.connect(db)
    cur = con.cursor()
    print("Connection Created to Database")
    cur.execute(''' CREATE TABLE IF NOT EXISTS tweets
                  (handle, tweet_text) ''')
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
    
    cur.execute('DELETE FROM tweets')
    con.commit()
    con.close()
    print("Table successfully deleted")
    
if __name__ == '__main__':
    """
    When run as a script, it will run the functions and ask user for an input of Y or N 
    to keep or drop the table they just created. 
    
    Input should be changed to allow for "would you like to create or update table, or drop etc...
    """
    
    create_table()
    add_tweets()
    input = input('Do you want to drop the table?\nY or N?\n')
    if input == 'Y' or input == 'y':
        drop_table()
        print("Thank you for using! This program will close now. Goodbye!")
    else:
        print("Thanks for using! Table has been saved!")
