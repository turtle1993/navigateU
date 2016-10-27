#coding=utf-8
from filter import filter
import MeCab
#from prettyprint import pp
import sys
from sentiment_analysis import get_sentiment

def analyze_sentence(raw_text):
    #    tagger = MeCab.Tagger('-ochasen')
    #tagger = MeCab.Tagger(" -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    tagger = MeCab.Tagger("/Users/hyb/Desktop/CHUANGZAO/mecab-ipadic-2.7.0-20070801")
    tagger.parse('')

    text,tag = filter(raw_text.encode("UTF-8"))
    node = tagger.parseToNode(text)
    words = []
    while node:
        word_type = node.feature.split(',')[0]
        if word_type == '動詞' or word_type == '形容詞':
            words.append(node.feature.split(',')[6])
        elif word_type == '名詞':
            words.append(node.surface)
        node = node.next
    
    while words.count("")>0:
        words.remove("")
    return words

def convert_senti(text):
	analyzed_words = analyze_sentence(text)
	senti = get_sentiment(analyzed_words)
        sentirank = judge_sentirank(senti)
	return sentirank


def convert_multitude_senti(text):
    sum=0
    for t in text:
        analyzed_words = analyze_sentence(t)
        sum=sum+get_sentiment(analyzed_words)
        print analyzed_words
    print sum
    sentiment=sum/len(text)
    sentirank = judge_sentirank(sentiment)
    return sentirank

def judge_sentirank(senti_value):
    positive_lowerlimit = 0

    if senti_value > positive_lowerlimit:
        rank = u"POSITIVE"
    elif senti_value < positive_lowerlimit:
        rank = u"NEGATIVE"
    else :
        rank = u"NORMAL"
    return rank
        
if __name__ == '__main__':
    senti = convert_senti(u"名古屋大学は悪い．汚い，不吉，気持ち悪い…．#名古屋 #愛知 http://nagoya.co.jp ")
    print senti
    
