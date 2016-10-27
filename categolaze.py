#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, math
import re

def getCategory(text):

    cate_book = ["暇","本読","読書","カフェ","新刊","書店","雨","引きこも","ひまだ","ブックオフ","読みたい","読みてー","の本","な本","漫画","マンガ","ジャンプ","サンデー","マガジン","チャンピオン","ブック","BOOK","わくわく","フィクション","小説","ラブコメ","SF","ライトノベル","ラノベ"]

    cate_food = ["腹減","空腹","はらぺこ","腹ペコ","ハラペコ","疲れ","つかれ","食べたい","お腹空","お腹す","はらへ","腹へ","くいてー","おいしそう","うまそう","美味しそう","旨そう","美味そう","ランチ","飲み会","むしゃくしゃ","ハンバーグ","ラーメン","パスタ","定食","アイス","卵","たまご","スイーツ","美味","味","美味しい","ご飯","飲みたい","飲み","ドリンク","ドリンクバー"]

    cate_movie = ["西島秀俊","ディズニー","監督","TSUTAYA","ツタヤ","ゲオ","GEO","見たい","見てー","鬱","暇","映画","コーラ","ポップコーン","かわいい","わくわく","ハリウッド","洋画","邦画","バルス","宮崎駿","ホラー","ラブコメ","SF","4D","映画館","ピカデリー","スクエア","ミリオン座","disney","mickey","デート","DVD","BD","レンタル"]

    book = 0
    food = 0
    movie = 0

    for pattern in cate_book:
        if pattern in text:
            book += 1
        
    for pattern in cate_food:
        if pattern in text: 
            food += 1
    
    for pattern in cate_movie:
        if pattern in text:
            movie += 1 

    max = 0
    if(food >= max):
        max = food
        cate = "food"
    if(book > max):
        max = book
        cate = "book"
    if(movie > max):
        max = movie
        cate = "movie"

    #print book
    #print food
    #print movie
    
    return cate

if __name__ == '__main__':
    text = "新刊で西島秀俊が引きこもりサンデー"
    print getCategory(text)

