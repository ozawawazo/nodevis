#coding:utf-8

directory = 'des/'

#f = open( directory + "mds-xmeans.json", "r")

x = []
y = []

for line in open( directory + "mds.csv"):

    a = line.rfind(r",")
    aa = line.find(r",")
    x.append(line[aa+1:a])
    y.append(line[a+1:])
    xval = line[aa+1:a]
    yval = line[a+1:]
    
print x[1]
print y

