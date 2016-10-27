import tweepy
import time
import sys
import connect2sql


def countdown(x):
    count = 0
    while (count < x):
        ncount = x - count
        sys.stdout.write("\r%d " % ncount)
        sys.stdout.flush()
        time.sleep(1)
        count += 1

def get_follower(TwitAPI,screen_name):
    tmp=[]
    i=0
    for follower in limit_handled(tweepy.Cursor(TwitAPI.followers, '@' + screen_name).items()):
        #f = follower.screen_name
        user_info = {'user_id':follower.id, 'user_name': "".join(follower.name.split('\'')) ,'user_screen_name': follower.screen_name}
        print user_info
        connect2sql.insert_usertest(user_info)
        tmp.append(user_info)
        i+=1
        print i
    # print api.user_timeline(f)
    print '\n'

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print "sleep now"
            countdown.countdown(15*60)
        except tweepy.TweepError as e:
            print e.reason
