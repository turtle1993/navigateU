# -*- coding: UTF-8 -*-
import sys
import csv
import random

reload(sys)
sys.setdefaultencoding('utf-8')

def get_Keywords(time,sentiment):
    # with open('category.txt','rb') as txtfile:
    #     for row in txtfile:
    #         print row

    with open('category_utf8.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',',quotechar='"')
        keywords=[]
        for row in list(reader):
            print row
     
            if row[0]==time and row[1]==sentiment:
                keywords= row[2:]
                print keywords

    keyword = keywords[random.randint(0, len(keywords) - 1)]
    
    return keyword



if __name__ == '__main__':
    time=(u"朝")
    sentiment=(u"NORMAL")
    keywords= get_Keywords(time,sentiment)
    print (keywords)

