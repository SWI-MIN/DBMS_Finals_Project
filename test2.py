import os,glob
import numpy as np

if not os.path.exists("temp"):
    os.mkdir('temp')

f = open("DB_students.csv",mode="r",encoding="utf-8") #開檔
#46W比
batch_size=10000
last = False
# line = f.readline()
# while line:
    
#     line = f.readline()
#     x=line.split(',',2)
#     print (x[0])
data = []
line = f.readline()
while line:
    row = f.readline().split(",")
    if len(row)==1:
        last = True
        break
    data.append(row)
data = sorted(data,key = lambda x : int(x[0][1:]))
# print (data)
with open('shit.csv','w',encoding='big5') as finfile:
    for row in data:
        for i,d in enumerate(row):
            finfile.write(d)
            if i < 1:
                finfile.write(',')

f.close()