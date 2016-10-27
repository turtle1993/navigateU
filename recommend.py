#coding=utf-8
import connect2sql
import random,sys,datetime,time


reload(sys)
sys.setdefaultencoding('utf-8')

def recommend_res(keyword,user_id):
    result=connect2sql.select_restaurant(keyword,user_id)
    recommend= result[random.randint(0,len(result)-1)]
    #recommend= random.choice(result)
    record_recommend(user_id, recommend[0])
    print recommend[0]
    return recommend[0].encode('utf-8').strip()

def recommend_film(user_id,mark):
    if mark==0:
        result=connect2sql.select_film_rank(user_id)
    else:result=connect2sql.select_film_sentiment(user_id)
    recommend = result[random.randint(0, len(result) - 1)]
    record_recommend(user_id, recommend[0])
    #print recommend[2].strftime('%a')
    return recommend[0].encode('utf-8').strip()


def record_recommend(user_id,recommend):
    connect2sql.insert_record(user_id,recommend)


if __name__ == '__main__':
    print recommend_film("居酒屋",3232562570)
    print recommend_film("3287501",0)

