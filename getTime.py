#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, math
import tweepy
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import defaultdict
import GetUserTweet
import GetUserFollow
import connect2sql
from pytz import timezone
import datetime
import calendar

def getTime(time):
    time = time + datetime.timedelta(hours=9)
    hour = time.hour
    #print hour
    if( 6 > hour ):
        time_zone = "深夜"
    elif( 10 > hour ):
        time_zone = "朝"
    elif( 15 > hour ):
        time_zone = "昼"
    elif( 18 > hour ):
        time_zone = "おやつ"
    elif( 23 > hour ):
        time_zone = "夜"
    else:
        time_zone = "深夜"
    #print time_zone
    return time_zone

def getDate(time):
    time = time + datetime.timedelta(hours=9)
    #week = datetime.weekday(time)
    
    year = time.year
    month = time.month
    day = time.day
    week = calendar.weekday(year,month,day)
    #print week
    return week



if __name__ == '__main__':

    consumer_key='hFOPObym5EewnOpjuGwJtqUMo'
    consumer_secret='TinxYYZyvfew5DBy2XXIbFahQ00H2KQiPsjp08qcWHEyqDd5uG'
    access_token_key='1495234620-O1sdYOM5JoOwGwdXLGKCPmh9d4qK3nYp4TUR2oq'
    access_token_secret='Xz3yRHCG0epncYqSAGkTqUHveBRPR5XCkLdoBuoJnlPBA'


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    #auth = tweepy.BasicAuthHandler("FSouzou2016","sozo2016F")
    api = tweepy.API(auth)


    id_list = []

    timeline=api.mentions_timeline()
    
    #    print timeline
    
    for status in timeline:
        #print status
        status_id=status.id
        
        if status_id not in id_list:
            screen_name=status.author.screen_name.encode("UTF-8")
            print "time:",status.created_at
            time = getTime(status.created_at)
            date = getDate(status.created_at)
            
            id_list.append(status_id) 

