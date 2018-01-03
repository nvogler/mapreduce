#!/usr/bin/python
import sys
import os

outfile = open('mapreduce/count.txt', 'w')
numDoc = 0
docsWord = {}
wordMap = {}
for line in sys.stdin:
	numDoc +=1
	print line.rstrip()
	data = line.split()
	docId = data.pop(0)
	for x in data:
		if x in wordMap:
			if docId not in docsWord[x]:
				wordMap[x] += 1
				docsWord[x][docId] = 1
		else:
			wordMap[x] = 1
			docsWord[x] = {}
			docsWord[x][docId] = 1
	print (line.rstrip())

outfile.write(str(numDoc) + '\n')
for x in wordMap:
	outfile.write(x + '\t' + str(wordMap[x]) + '\n')