from requests_oauthlib import OAuth1Session
import tweepy
import json
with open('twitter.json') as f:
  twitter_keys = json.load(f)

CONSUMER_KEY = twitter_keys['consumer_key']
CONSUMER_SECRET = twitter_keys['consumer_secret']
ACCESS_TOKEN_KEY = twitter_keys['access_token']
ACCESS_TOKEN_SECLET = twitter_keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECLET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    if 'media' in tweet.entities:
        for media in tweet.extended_entities['media']:
            media_url = media['media_url']
            print(media_url)
