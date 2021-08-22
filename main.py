import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from requests_oauthlib import OAuth1Session
import tweepy
import requests
import json
with open('twitter.json') as f:
  twitter_keys = json.load(f)

def main():
  CONSUMER_KEY = twitter_keys['consumer_key']
  CONSUMER_SECRET = twitter_keys['consumer_secret']
  ACCESS_TOKEN_KEY = twitter_keys['access_token']
  ACCESS_TOKEN_SECLET = twitter_keys['access_token_secret']

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECLET)

  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  public_tweets = api.home_timeline()

  img_urls = []

  for tweet in public_tweets:
    if 'media' in tweet.entities:
        for media in tweet.extended_entities['media']:
            media_url = media['media_url']
            img_urls.append(media_url)

  for i in range(0,len(img_urls)):
    url = img_urls[i]
    file_name = f"./images/{i}.jpg"
    response = requests.get(url)
    img = response.content
    with open(file_name, "wb") as f:
      f.write(img)

  for i in range(0,len(img_urls)):
    img = Image.open(f'./images/{i}.jpg')
    st.image(img, use_column_width=True)

if __name__ == "__main__":
  main()
