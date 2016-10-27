#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
import sys, os,uuid

user = 'root'
pwd  = 'souzou2016'
host = '127.0.0.1'
db   = 'twitter_sentiment'



def insert_userinfo(user_info):
    select_sql=("select * from user_info where user_id={}".format(user_info['user_id']))
    #print select_sql
    if search_data(select_sql):
        return 0
    insert_sql=("INSERT INTO user_info(user_id,screen_name,user_name) VALUES({0},'{1}','{2}')".format(
            user_info['user_id'],user_info['user_screen_name'],user_info['user_name']))
    #print insert_sql
    insert_data(insert_sql)
    return 1


def insert_twittertext(twitter):
    select_sql = ("select * from twitter_text where twitter_id='{}'".format(twitter['tweet_id']))
    if search_data(select_sql):return

    #tweet_id=uuid.uuid1()
    sql_text=("INSERT INTO twitter_text(twitter_id,text) VALUES('{0}','{1}')".format(
            twitter['tweet_id'],twitter['text']))
    print sql_text
    try:
        insert_data(sql_text)
    except:
        return

    sql_sentiment = ("INSERT INTO sentiment(user_id,twitter_id,time,sentiment) VALUES('{0}','{1}','{2}','{3}')".format(
        twitter['user_id'],twitter['tweet_id'], twitter['time'],twitter['sentiment']))
    insert_data(sql_sentiment)


def insert_usertest(user_info):
    select_sql = ("select * from user_test where user_id={}".format(user_info['user_id']))
    if search_data(select_sql):
        update_sql=("update user_test set times=times+1 where user_id='{}'".format(user_info['user_id']))
        update_data(update_sql)
    else:
        insert_sql = ("INSERT INTO user_test(user_id,screen_name,user_name,times) VALUES({0},'{1}','{2}',1)".format(
        user_info['user_id'], user_info['user_screen_name'],user_info['user_name']))
        insert_data(insert_sql)
    return 1

def search_user_test(text_bool):
    if text_bool==1:
        select_sql=("SELECT sentiment.user_id,sentiment.twitter_id,sentiment.time,sentiment.sentiment,twitter_text.text from sentiment join twitter_text on sentiment.twitter_id=twitter_text.twitter_id where time>'2016-01-01' ")
    else:
        select_sql=  ("SELECT sentiment.user_id,sentiment.twitter_id,sentiment.time,sentiment.sentiment,twitter_text.text from sentiment join twitter_text on sentiment.twitter_id=twitter_text.twitter_id where time>'2016-01-01' ")
    return search_data(select_sql)

def insert_dictionary(word_dic):
    sql=("insert into word_sentiment(word,value) values('{0}',{1})").format(word_dic['word'],word_dic['value'])
    print sql
    insert_data(sql)

def select_dictionary():
    sql="select * from word_sentiment"
    return search_data(sql)

def insert_propernoun(result):
    for res in result:
        select_sql=("select * from porpernoun where word='{0}'").format(res[0])
        if search_data(select_sql):
            update_sql=("update porpernoun set times=times+1,value=value+{1},result=value/times where word='{0}'").format(res[0],res[1])
            update_data(update_sql)
        else:
            insert_sql=("insert into porpernoun(word,value,times,result) values('{0}',{1},1,{1})").format(res[0],res[1])
            #print insert_sql
            insert_data(insert_sql)

def update_sentiment(tweet_sentiment):
    update_sql=("update sentiment set sentiment={1} where twitter_id={0}").format(tweet_sentiment[0],tweet_sentiment[1])
    update_data(update_sql)

def search_usertest(target):
    if target=="":
        sql=("select * from user_test")
    else:    sql=("select * from user_test where user_id='{}'".format(target))
    return search_data(sql)



def insert_film(films):
    for film_info in films:
        select_sql=("select * from film_info where film_name='{0}'").format(film_info[0])
        if search_data(select_sql):
            update_sql=("update film_info set rank={1},time='{2}' where film_name='{0}'").format(film_info[0],film_info[1],film_info[2])
            update_data(update_sql)
        else:
            insert_sql=("insert into film_info(film_name,rank,time,sentiment) values('{0}','{1}','{2}',0)" ).format(film_info[0],film_info[1],film_info[2])
            insert_data(insert_sql)

def insert_filmname(name_list):
    for name in name_list:
        insert_sql=("insert into film_info(film_name) values('{0}')").format(name)
        insert_data(insert_sql)

def select_restaurant(keyword,user_id):
    select_sql=("select * from restaurants where catalogue like '%{0}%' and restaurant not in (select recommend from record_recommend where user_id={1})").format(keyword,user_id)
    return search_data(select_sql)

def insert_record(user_id,recommend):
    insert_sql=("insert into record_recommend(user_id,recommend) values('{0}','{1}')").format(user_id,recommend)
    insert_data(insert_sql)

def select_film_rank(user_id):
    select_sql=("select * from film_info where rank>0 and film_name not in (select recommend from record_recommend where user_id={0})").format(user_id)
    return search_data(select_sql)

def select_film_sentiment(user_id):
    select_sql = ("select * from film_info where sentiment>0 and film_name not in (select recommend from record_recommend where user_id={0})").format(user_id)
    return search_data(select_sql)


'''database controller'''



def insert_data(sql):
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    insert_sql = sql
    try:
        cursor.execute(insert_sql)
    except mysql.connector.Error as err:
        print("insert table 'mytable' failed.")
        print("Error: {}".format(err.msg))
        sys.exit()
    cnx.commit()
    cursor.close()
    cnx.close()



def search_data(sql):
    cnx = mysql.connector.connect(user=user,password=pwd,host=host,database=db)
    cursor = cnx.cursor()
    search_sql=sql
    try:
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

    except mysql.connector.Error as err:
        print("Error:{}".format(err.msg))
        sys.exit()

    cnx.commit()
    cursor.close()
    cnx.close()
    return results

def update_data(sql):
    cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = cnx.cursor()
    search_sql = sql
    try:
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print("Error:{}".format(err.msg))
        sys.exit()

    cnx.commit()
    cursor.close()
    cnx.close()

