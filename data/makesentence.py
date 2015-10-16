#coding:utf-8

import json
import csv
import codecs

directory = 'change/'

f = open( directory + "data.json", "r")
fout = codecs.open( directory + "egm_sentence.txt", "w", "utf-8")
jsonData = json.load(f)

for var in jsonData[u"nodes"]:
    fout.write(var[u"text"])
    fout.write("\n")
