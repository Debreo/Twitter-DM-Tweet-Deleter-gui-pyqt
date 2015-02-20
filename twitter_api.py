__author__ = 'Danelle'

import sys, time
import tweepy
from random import randint


def delete_tweets(CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET):

    """Deletes 3 Tweets From Timeline"""

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    counter = 3
    timeline = api.user_timeline(count = counter)

    for t in timeline:
        api.destroy_status(t.id)
    print "Total Tweets Removed = ", counter



def dm(users, messages, CONSUMER_KEY,CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    """Takes in text documents from GUI and sends a DM of inputed text to users
        who are following back"""


    for user in users:
        user = user.strip()
        message = user + " "
        for mess in messages:
            try:
                mess = mess.strip()
                text = mess + " "
                print(message, text)
                api.send_direct_message(message, text = text)
            except:
                print("********************ERROR*********************************")
                print("Can't message %sbecause he's not following you") % (message)
                print("********************ERROR*********************************")

            finally:
                timeout = randint(1, 8)
                time.sleep(timeout)




