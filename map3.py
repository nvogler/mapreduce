#!/usr/bin/python
import os
import sys
import math

#reads in big N
wordLittleN = {}
with open('mapreduce/count.txt', 'r') as data:
	bigN = float(data.readline())
	for x in data:
		count = x.split()
		wordLittleN[count[0]] = float(count[1])

for line in sys.stdin:
	#article variables for sorting intermediate data
	outputList = []
	docScore = 0
	i = 0
	#converts article to a list of the words in it (has duplicates)
	words = line.split()
	docId = words.pop(0)
	length = len(words)
	while (i + 1) < length:
		littleN = wordLittleN[words[i]]
		docFreq = int(words[i + 1])
		idf = math.log10(bigN / littleN)
		weight = (docFreq**2) * (idf**2)
		docScore += weight
		output = words[i] + '\t' + str(idf) + '\t' + str(littleN) + '\t' + docId + '\t' + str(docFreq)
		outputList.append(output)
		i += 2
	for x in outputList:
		print x + '\t' + str(docScore)
