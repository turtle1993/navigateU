#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, math
import random
import recommend


def makeText(cate,date,time,word):
    
    
    if(cate == 'book'):
        if(date == '5' or date == '6'):
           text = random.choice(["暇なら{word}がおすすめよ".format(**locals()),"うええ"])
        else:
            if(time == '夜'):

                text = "aaaa"
#*********************************************************

    if(cate == 'food'):
        if(time == '朝'):
           text = random.choice(["暇なら"+word+"がおすすめよ","おはよう、朝は"+word+"がおすすめです。"])
        elif(time == '昼'):
            text = random.choice(["おなかすいた？"+word+"がおすすめよ","お昼は、"+word+"で食べない？"])
        elif(time == 'おやつ'):
            text = random.choice(["おやつは{word}がおすすめよ".format(**locals()),"小腹が空いたら{word}に行こう！".format(**locals()),"一休みして{word}でもどうだろう？".format(**locals())])
        elif(time == '夜'):
            text = random.choice(["夜は{word}がおすすめです".format(**locals()),"{word}って言うお店が美味しいみたいです".format(**locals()),"今夜は{word}で夕飯を食べるのはいかがですか？".format(**locals())])
        else:
            text = random.choice(["夜遅くまでお疲れ様！今日はもう寝よう！","かっこいい松山さんを思い浮かべながら、寝るのがオススメ","おやすみ！"])

    return text




