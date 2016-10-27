#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, math
import tweepy
import sys
import time as timesleep
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import defaultdict
from GetUserTweet import get_user_tweet
import GetUserFollow
import connect2sql
import repTemplate
import categolaze
import getTime
#from convert_senti import convert_senti
from convert_senti import convert_multitude_senti
#from prettyprint import pp
from keyword import iskeyword as is_python_keyword
from get_Keywords import get_Keywords
import recommend

"""
consumer_key='ipSu2CzBIB20OS5EGcYNheC1M'
consumer_secret='qQaIJjlb8LrhGoAktGKl73cceRlnMEj2LIqqlrxHVvNcPlo7Zn'
access_token_key='729572511109644288-pPDDhEMTrIWDn0OIXZvbhMniekCV1aY'
access_token_secret='4RXMFwrwdgcBILjRRiFqdna7bC2yg9oYhrfipbGJGpseo'
"""

consumer_key='hFOPObym5EewnOpjuGwJtqUMo'
consumer_secret='TinxYYZyvfew5DBy2XXIbFahQ00H2KQiPsjp08qcWHEyqDd5uG'
access_token_key='1495234620-O1sdYOM5JoOwGwdXLGKCPmh9d4qK3nYp4TUR2oq'
access_token_secret='Xz3yRHCG0epncYqSAGkTqUHveBRPR5XCkLdoBuoJnlPBA'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

#auth = tweepy.BasicAuthHandler("FSouzou2016","sozo2016F")
api = tweepy.API(auth)


#main

id_list = []
i=0
while (i==0):
        #id_list != [] -> repray recommendation  
        try:
                timeline=api.mentions_timeline(count=10)
        except tweepy.RateLimitError:
                print "ERROR"
                

        for status in timeline:
            status_id=status.id

        
            if status_id not in id_list:
                screen_name=status.author.screen_name.encode("UTF-8")
                cate = categolaze.getCategory(status.text)
                time = getTime.getTime(status.created_at)
                date = getTime.getDate(status.created_at)
                #senti = convert_senti(status.text)
                #senti = (u"POSITIVE")
                print "mentiontext:"+status.text
                print status.id
                print screen_name

                """user全部tweet"""
                text=[]
                text= get_user_tweet(api,screen_name)
                text.append(status.text)
                # print text
                # for t in text:
                #     print t
                senti=convert_multitude_senti(text)
                """user全部tweet"""


                print time,screen_name
                restaurant_cate = get_Keywords(time,senti)
                #restaurant_cate = "うなぎ"
                print  cate, time, date,senti, restaurant_cate
                #user_id = status.entities[u"user_mentions"][u"id"]
                user_id = status.author._json[u'id']
                print 'USER_ID=',user_id      
                word = recommend.recommend_res(restaurant_cate,user_id)
                reply_text="@"+screen_name+" aaa"+repTemplate.makeText(cate,date,time,word)
                api.update_status(status=reply_text,in_reply_to_status_id=status_id)
                id_list.append(status_id) 
        timesleep.sleep(5)
        i=1
    
