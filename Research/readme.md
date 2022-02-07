# Research/ Thought Process

The purpose of this project is to broaden our horizons and continue personal development towards the goal of a pursuance of Data Science.

I want to be able to develop an application that a user can log into and view tweets from a Congressional Member/Candidate. Ideally, we want to develop a way to see how campaign promises and platform goals are being met by these delegates via their social media presence. Can we tell fact from bull? Can we use this as a way to keep our delegates honest? 

To complete this project, we will pull from Twitter, tweets from the delegates and compare to campaign promises, looking for matching words/actions being taken. To do so, we will need to create models that can read the tweet and give an answer as to whether this is in line with their campaign or not. We will need to scrape for tweets, create a database, and make a model. Production of this would need to be done through Docker to an AWS BeanStalk. This would be the easiest way. App will have to continue scraping and all process will need to be automated. This will require the notebooks to be written as scripts.

Tweepy pulls data from twitter. Database to include all data from congress members. Data on platform. Model puts it all together.
Need to find a way to get data on platforms/campaign promises. May be able to find a dataset.