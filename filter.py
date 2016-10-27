#! /usr/bin/env python
#coding:utf-8

import sys
import re
tag = re.compile(u'[\#\＃].+?[\s\n\s　]')
taglast = re.compile(u'[\#\＃][^#]+$')
RT = re.compile(u'\RT\s@.+?\s')
rep = re.compile(u'\@.+?\s')
http = re.compile(u'http.?[0-9a-zA-Z\.\/\…]+')
https = re.compile(u'https.?[0-9a-zA-Z\.\/\…]+')
symbol = re.compile(u'\"|\*|\(|\)|\r')
def filter(text):
    tmp = RT.sub('',text)
    tmp = rep.sub('',tmp)
    tmp = https.sub('', tmp)
    tmp = http.sub('',tmp)

    tags = list(tag.findall(tmp))
    lasttags = list(taglast.findall(tmp))
    tags = tags + lasttags

    tmp = tag.sub('',tmp)
    tmp = taglast.sub('',tmp)
    tmp = symbol.sub('',tmp)
    tagtext = ','.join(tags)
    return tmp,tagtext

def tweetsplit(text):
    p = re.compile(r'。|\n|！| |　')
    tmp = re.split(r'。|．|\n|　',text)
    while tmp.count('')>0:
        tmp.remove('')
    return tmp

#
if __name__ == "__main__":
    text = u'RT @meidai TweetX\r\r\r\r\r#hashtagA #hashtagB http… http://meidai.co/Eijk5aE tweetY #hashtagC http//t.co/to0AtH… https://t.co/aJ9xcvMW6Y'
    #text = u'こだわりすぎて、ずっと買えなかった。ずっと悩んでいたリュック選び。でも、ふらっと立ち寄ったお店で決めてやった！ 高くないやつなら、もうある程度気に入りゃなんでもいいやと！\n脳内会議の結果、紺に決定！ '
    #text = u'実質0円で導入可能な防災対応のデジタルサイネージ付き自販機 　＃デジタルサイネージ　＃ニュース '
    print 'TEXT',text,type(text)
    
    print '=============='
    text,tag = filter(text)
    print 'FILTED_TEXT='+text,'TAG='+tag

    print '=============='
    text = tweetsplit(text)
    for i,t in enumerate(text):
        print 'NUMBER=',i,'SENTENCE=',t
    
