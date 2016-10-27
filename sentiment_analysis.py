# coding=utf-8
import connect2sql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
dictionary=[]
for word in connect2sql.select_dictionary():
     dictionary.append([word[0].encode('utf-8'),word[1]])
     #print word[0],word[1]

pn_dict=dict(dictionary)
# print pn_dict

#pn_dict = {data['word']: data['value'] for data in connect2sql.select_dictionary({},{'word':1,'value':1})}
# pn_dict = {data[0] :data[1] for data in connect2sql.select_dictionary()}
# for word in pn_dict:
#     print word


def isexist_and_get_data(data, key):
    return data[key] if key in data else None


def get_sentiment(word_list):
    val = 0
    score = 0
    word_count = 0
    val_list = []
    for word in word_list:
        val = isexist_and_get_data(pn_dict, word)
      #  print val
        val_list.append(val)
        if val is not None and val != 0: # 見つかればスコアを足し合わせて単語カウントする
            score += val
            word_count += 1
        # print score
        # print round(score/float(word_co
            # unt),2)

    # logger.debug(','.join(word_list).encode('utf-8'))
    # logger.debug(val_list)
    return round(score/float(word_count),2) if word_count != 0. else 0.

if __name__ == '__main__':
    print get_sentiment(['あがく','過去','明日'])
