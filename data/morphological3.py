#coding:utf-8

#これはegm_lf.txtの文列を形態素解析し、出力で文、類似度、単語を出力する
#import os

import sys
import MeCab
import csv
import json
directory = 'change/'


def extractKeyword(text):
    tagger = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/unidic")
    encoded_text = text.decode('utf-8').encode("utf-8")
    encoded_node = tagger.parseToNode(encoded_text)
    keywords = []
    stopword = ["0", "1", "2", "5"]
    while encoded_node:
        encoded_node_surface = encoded_node.surface.decode("utf-8")
        encoded_node_feature = encoded_node.feature.decode("utf-8")
        enco = encoded_node_feature.split(",")
        if encoded_node.surface.decode("utf-8") != ",":
            if encoded_node_feature.split(",")[0] == u"名詞":
                if enco[10] != "0" and enco[10] != "1" and enco[10] != "2" and enco[10] != "3" and enco[10] != "5":
                    keywords.append(encoded_node_feature.split(",")[10])
            if encoded_node_feature.split(",")[0] == u"動詞":
                keywords.append(encoded_node_feature.split(",")[7])
            if encoded_node_feature.split(",")[0] == u"形容詞":
                keywords.append(encoded_node_feature.split(",")[7])
            if encoded_node_feature.split(",")[0] == u"形容動詞":
                keywords.append(encoded_node_feature.split(",")[7])
        encoded_node = encoded_node.next
    return keywords

f  = open( directory + "mor-words.csv", "w") #egmresult2.csv
f2 = open( directory + "mor-node_words.csv", "w") #egmresult.csv
f3 = open( directory + "mor-node_words_weight.csv", "w")
f4 = open( directory + "unidic.csv", "w")
f5 = open( directory + "word-sentence.csv", "w")
f6 = open( directory + "words.csv", "w")

csv.writer(f3).writerow(["weight","sentence","a","b","c","d","e","f","g","h","i","j"])
csv.writer(f4).writerow(["name"])
csv.writer(f5).writerow(["word","sen1","sen2","sen3","sen4","sen5","sen6","sen7","sen8","sen9"])
csv.writer(f6).writerow(["a","b","c","d","e","f","g","h","i","j"])
list = []

fread = open( directory + "data.json", "r")
jsonData = json.load(fread)
count = 0
list5 = []
for line in open( directory + "egm_sentence.txt"):
    list2 = []
    list3 = []
    list6 = []
    line = line.replace('\n','')
    line = line.replace('\r','')
    count2 = 0
    for var in jsonData[u"nodes"]:
        if count == count2:
            count2 = count2 + 1
            list3.append(var[u"weight"])
        else:
            count2 = count2 + 1
            continue
        list2.append(line)
        list3.append(line)
    keywords = extractKeyword(line)
    for w in keywords:
        list4 = []
        list55 = []
        if w.encode('utf-8') in list:
            nomeaning = 0
        else:
            list.append(w.encode('utf-8'))
        list2.append(w.encode('utf-8'))
        list3.append(w.encode('utf-8'))
        list4.append(w.encode('utf-8'))
        print w.encode('utf-8')
        list55.append(w.encode('utf-8'))
        list6.append(w.encode('utf-8'))
        list55.append(line)
        list5.append(list55)
        csv.writer(f4).writerow(list4)
    count = count + 1
    csv.writer(f2).writerow(list2)
    csv.writer(f3).writerow(list3)
    csv.writer(f6).writerow(list6)
csv.writer(f).writerow(list)

wordsentence =[]
for d in list5:
    count = 0
    for dd in wordsentence:
        if (dd[0] == d[0]):
            dd.append(d[1])
            count += 1
    if count == 0:
        wordsentence.append(d)
for d in wordsentence:
        csv.writer(f5).writerow(d)
