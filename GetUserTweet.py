# -*- coding: utf-8 -*-

import tweepy
import countdown
import connect2sql



consumer_key='hFOPObym5EewnOpjuGwJtqUMo'
consumer_secret='TinxYYZyvfew5DBy2XXIbFahQ00H2KQiPsjp08qcWHEyqDd5uG'
access_token_key='1495234620-O1sdYOM5JoOwGwdXLGKCPmh9d4qK3nYp4TUR2oq'
access_token_secret='Xz3yRHCG0epncYqSAGkTqUHveBRPR5XCkLdoBuoJnlPBA'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

def get_user_tweet(TwitAPI,screen_name):
    text=[]
    follow_tweet =TwitAPI.user_timeline(screen_name=screen_name)
    for tweet in follow_tweet:
        #print tweet.text
        text.append(tweet.text)

    return text


def get_tweet(TwitAPI,user_id_list):
    i=0
    for user_id in user_id_list:
        try:
            follow_tweet =TwitAPI.user_timeline(id=user_id)

            #for tweet in limit_handled(tweepy.Cursor(TwitAPI.user_timeline(screen_name=screen_name)).items()):
                #tweepy.process_page(tweet)
            for tweet in follow_tweet:

                # print tweet
                # print tweet.user.name
                # print tweet.user.screen_name
                # print tweet.text
                # print tweet.created_at
                # print tweet.id
                i=i+1
                print i
                tweet_info={'user_id':tweet.user.screen_name,'tweet_id':tweet.id,'time':tweet.created_at,'sentiment':'0', 'text':"".join(tweet.text.split('\''))}
                print tweet_info
                connect2sql.insert_twittertext(tweet_info)
        except tweepy.RateLimitError:
            print "sleep now"
            countdown.countdown(15*60)
        except tweepy.TweepError as e:
            print("Failed to run the command on that user, Skipping...")
            print e.reason

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print "sleep now"
            countdown.countdown(15*60)
        except tweepy.TweepError:
            print tweepy.TweepError