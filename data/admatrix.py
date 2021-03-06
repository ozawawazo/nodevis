#coding:utf-8
import json
import csv
import numpy
from numpy  import *

#this pyfile make 1"sentence-sentence matrix csv file" 2"make word-word MDSfile"

directory = 'change/'
File = 'WBU.txt'

f = open( directory + 'data.json', 'r')
fout = open( directory + 'node-admatrix.csv', 'w')
fpos = open( directory + 'mds.csv', 'w')
fnpos = open( directory + 'tagplace.csv', 'w')
csvWriter = csv.writer(fout)
posWriter = csv.writer(fpos)
nposWriter = csv.writer(fnpos)

#make sentence-sentence matrix list
admatrix = []
jsonData = json.load(f)
count = 0
for var in jsonData[u"nodes"]:
    admatrix.append([])
    for var2 in jsonData[u"nodes"]:
        admatrix[count].append(1)
    count = count + 1
minvalue = 1
for var in jsonData[u"links"]:
    if jsonData[u"nodes"][var[u"source"]][u"weight"] > jsonData[u"nodes"][var[u"target"]][u"weight"]:
        value = jsonData[u"nodes"][var[u"target"]][u"weight"]
    else:
        value = jsonData[u"nodes"][var[u"source"]][u"weight"]
    value = 1.0 / (value + 1)
    if value != 0:
        if minvalue > value:
            minvalue = value
    admatrix[var[u"source"]][var[u"target"]] = value
    admatrix[var[u"target"]][var[u"source"]] = value
for var in jsonData[u"links"]:
    admatrix[var[u"source"]][var[u"target"]] = admatrix[var[u"source"]][var[u"target"]] + minvalue
    admatrix[var[u"target"]][var[u"source"]] = admatrix[var[u"target"]][var[u"source"]] + minvalue
for a in admatrix:
    csvWriter.writerow(a)
f.close()
fout.close()

#make word-sentence matrix
f = open( directory + 'mor-node_words.csv', 'rb')#文と単語の配列
dataReader = csv.reader(f)
listData = []
count = 0
for row in dataReader:
    f2 = open( directory + 'mor-words.csv', 'rb')#単語リスト
    dataReader2 = csv.reader(f2)
    for word in dataReader2:
        listData.append([])
        for w in word:
            if w in row:
                listData[count].append(1)
            else:
                listData[count].append(0)
        count = count + 1

#make word-word matrix
ssmatrix = numpy.array([[float(v) for v in row] for row in admatrix])
I = numpy.matrix(numpy.identity(len(admatrix)))
Inverse_ssmatrix = numpy.linalg.inv(I - ssmatrix)
wsmatrix = numpy.array([[float(v) for v in row] for row in listData])
wwmatrix = wsmatrix.T.dot(Inverse_ssmatrix).dot(wsmatrix)
#print ssmatrix
#print I
#print Inverse_ssmatrix
#print wsmatrix

f3 = open( directory + File)
lines2 = f3.read()

wwmatrix3 = matrix(lines2)
#print wwmatrix3
#print type(wwmatrix3)
#wwmatrix2 = []
#for line in lines2:
#    line2 = map(float, line)
#    wwmatrix2.append(line2)
#wwmatrix3 = numpy.array(wwmatrix2)
f3.close()

    
#print wwmatrix
#print type(wwmatrix)



#make MDS
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

similarities = wwmatrix3
seed = numpy.random.RandomState(seed=3)
mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed, dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_
count = 0
f2 = open( directory + 'mor-words.csv', 'rb')#単語リスト
dataReader2 = csv.reader(f2)
posWriter.writerow(["tag","x","y"])
for word in dataReader2:
    for a in pos:
        print a
        print word[count]
        samplelist = [word[count]]#insert word
        for aa in a:
            samplelist.append(aa)#insert position
        posWriter.writerow(samplelist)
        count = count + 1

#f3 = open('mor-node_words_weight.csv', 'rb')#単語リスト
#dataReader3 = csv.reader(f3)
#posWriter.writerow(["tag","prex","prey","weight","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
#for word in dataReader2:
#    for a in pos:
#        samplelist = [word[count]]#insert word
#        for aa in a:
#            samplelist.append(aa)#insert position
#        #wordが入ってる文を探し、過頻度をカウントする
#        countfre = 0
#        insertsen = []
#        insertsen2 = []
#        f3 = open('pen/mor-node_words_weight.csv', 'rb')#単語リスト
#        dataReader3 = csv.reader(f3)
#        countrabel = 0
#        for tab in dataReader3:
#            if countrabel == 0:
#                countrabel = countrabel
#            else:
#                for tab2 in tab:
#                    if word[count] == tab2:
#                        countfre = countfre + int(tab[0])
#                        insertsen.append(tab[1])
#            countrabel = countrabel + 1
#        samplelist.append(countfre)
#        for insertsen1 in insertsen:
#            samplelist.append(insertsen1)
#        posWriter.writerow(samplelist)
#        count = count + 1
