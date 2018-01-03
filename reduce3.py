#!/usr/bin/python
import sys
import os

wordMap = {}
wordTotal = {}
wordIdf = {}
docsSeen = {}
for line in sys.stdin:
	data = line.split()
	word = data[0]
	idf = data[1]
	littleN = data[2]
	
	if word not in wordMap:
		wordMap[word] = ""
		docsSeen[word] = {}
		wordTotal[word] = 0
		wordIdf[word] = idf
	length = len(data)
	i = 3
	while (i + 2) < length:
		if data[i] not in docsSeen[word]:
			wordMap[word] += data[i] + '\t' + data[i + 1] + '\t' + data[i + 2] + '\t'
			docsSeen[word][data[i]] = 1
		wordTotal[word] = littleN
		i += 3
for x in wordMap:
	output = x + '\t' + str(wordIdf[x]) + '\t' + wordTotal[x] + '\t' + wordMap[x]
	print output