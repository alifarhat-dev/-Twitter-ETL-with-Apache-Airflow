import tweepy
import pandas as pd
from datetime import datetime
import s3fs
import json
access_key = "tkyx6Z3VnSnX9BIs27T5FjHvi"
access_secret = "XDSAKfqBUwkpMYacQ2j5AFqY5bze6VBLZxdgLzBkMW8SAyLEJf"
consumer_key = "1669471059937046528-02GGRC6BepLB4jF9EO4aWiqjY6crtT"
consumer_secret = "Ok6a3RPljbrvgy8be9DHVgfaad2vEpHpV685ShxOjFS4Z"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name=
                           "elonmusk",
                           count=200,
                           include_rts=False,
                           tweet_mode="extended"
                           )
tweets_data = []
for tweet in tweets:
    text = tweet.json['full_text']
    refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
    tweets_data.append(refined_tweet)
df = pd.DataFrame(list)
df.to_csv('refined_tweets.csv')