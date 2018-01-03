#!/usr/bin/python
import sys
import os

#2d map docInfo[docID][word] = wordFreq (within doc)
docInfo = {}
docList = []

#INPUT
for line in sys.stdin:
	#converts word/wordinfo to list
	#word - current(nk) - freq
	data = line.split()
	docId = data.pop(0)
	docList.append(docId)
	#temp maps for word/freq and little n sub k
	wordMap = {}
	length = len(data)
	i = 0
	while (i + 2) < length:
		wordMap[data[i]] = int(data[i + 2])
		i += 3
	#saves to doc
	docInfo[docId] = wordMap

#OUTPUT
#docs
for x in docList:
	#words in this doc, no dups
	output = x + '\t'
	for y in docInfo[x]:
		output += y + '\t' + str(docInfo[x][y]) + '\t'
	print (output.rstrip())